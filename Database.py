import sqlite3

class Database:

    def __init__(self, path):
        self.connection=sqlite3.connect(path)
        self.cursor=self.connection.cursor()

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()
    
    def get_cursor(self):
        return self.cursor