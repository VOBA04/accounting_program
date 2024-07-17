from Database import Database
import hashlib

class User:
    def __init__(self, database:Database):
        self.db=database
        self.cursor=database.get_cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS User(
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL)
                            """)
        
    def add_user(self, username:str, password:str):
        self.cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).hexdigest()))
        self.db.commit()

    def chech_user(self, username:str, password:str):
        self.cursor.execute("SELECT username, password FROM User WHERE username=? AND password=?",(username, hashlib.sha256(password.encode()).hexdigest()))
        result = self.cursor.fetchone()
        return result!=None
    
    def trunc(self):
        self.cursor.execute("DELETE FROM User")
        self.db.commit()