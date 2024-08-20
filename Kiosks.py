from Database import Database


class Kiosks:
    def __init__(self, database: Database):
        self.db = database
        self.cursor = database.get_cursor()
        self.cursor.execute(
            """
                            CREATE TABLE IF NOT EXISTS Kiosks(
                            id INTEGER PRIMARY KEY,
                            number INTEGER UNIQUE)
                            """
        )
        self.cursor.execute("SELECT * FROM Kiosks")
        columns = self.cursor.description
        if columns.count == 2:
            self.cursor.execute("SELECT item FROM Items")
            items = self.cursor.fetchall()
            for item in items:
                sql_str = f"""
                            ALTER TABLE Kiosks
                            ADD COLUMN {item[0]} INTEGER DEFAULT 0
                            """
                self.cursor.execute(sql_str)
        self.db.commit()

    def add_kiosk(self, number: int):
        try:
            self.cursor.execute("INSERT INTO Kiosks (number) VALUES (?)", (number,))
        except:
            return False
        return True

    def add_kiosks(self, numbers: tuple):
        try:
            self.cursor.executemany("INSERT INTO Kiosks (number) VALUES (?)", numbers)
        except:
            return False
        return True

    def delete_kiosk(self, number: int):
        self.cursor.execute("DELETE FROM Kiosks WHERE number=?", (number,))

    def delete_kiosks(self, numbers: tuple):
        self.cursor.executemany("DELETE FROM Kiosks WHERE number=?", numbers)

    def get_kiosks(self):
        self.cursor.execute("SELECT * FROM Kiosks")
        kiosks = self.cursor.fetchall()
        kiosks_list = []
        columns = self.cursor.description
        items = []
        for column in columns:
            items.append(column[0])
        kiosk_dict = {}
        for kiosk in kiosks:
            i = 0
            for item in items:
                kiosk_dict[item] = kiosk[i]
                i += 1
            kiosks_list.append(kiosk_dict)
        return kiosks_list

    @staticmethod
    def db_to_dict(db: Database, id: int):
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM Kiosks WHERE id=?", (id,))
        kiosk = cursor.fetchone()
        columns = cursor.description
        items = []
        for column in columns:
            items.append(column[0])
        kiosk_dict = {}
        i = 0
        for item in items:
            kiosk_dict[item] = kiosk[i]
            i += 1
        return kiosk_dict
