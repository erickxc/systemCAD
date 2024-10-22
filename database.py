import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sistema_academico.db')
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
