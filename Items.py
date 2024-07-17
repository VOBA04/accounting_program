from Database import Database

class Items:
    def __init__(self, database:Database):
        self.db=database
        self.cursor=database.get_cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Items(
                            id INTEGER PRIMARY KEY,
                            item TEXT UNIQUE,
                            quantity INTEGER NOT NULL)
            """)
        
    def add_item(self, item:str, quantity=0):
        try:
            self.cursor.execute("INSERT INTO Items (item, year_quantity) VALUES (?, ?)", (item, quantity))
        except:
            return False
        # self.db.commit()
        return True
    
    def delete_item(self, item:str):
        self.cursor.execute("DELETE FROM Items WHERE item=?", (item,))
        # self.db.commit()

    def change_quantity(self, item:str, quantity:int):
        self.cursor.execute("UPDATE Items Set quantity=? WHERE item=?", (quantity, item))
        # self.db.commit()

    def change_item(self, old_item:str, new_item:str):
        self.cursor.execute("UPDATE Items Set item=? WHERE item=?", (new_item, old_item))
        # self.db.commit()