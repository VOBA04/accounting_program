from Database import Database

class Kiosks:
    def __init__(self, database:Database):
        self.db=database
        self.cursor=database.get_cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Kiosks(
                            id INTEGER PRIMARY KEY,
                            number INTEGER UNIQUE)
                            """)
        # self.cursor.execute("SELECT COUNT(*) FROM Items")
        # items_count=self.cursor.fetchone()[0]
        self.cursor.execute("SELECT item FROM Items")
        items=self.cursor.fetchall()
        for item in items:
            sql_str=f"""
                        ALTER TABLE Kiosks
                        ADD COLUMN {item[0]} INTEGER
                        ADD COLUMN {item[0]+"_quantity"} INTEGER
                        FOREIGN KEY {item[0]} REFERENCES Items(id)
                        """
            self.cursor.execute(sql_str)