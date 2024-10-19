import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sistema_academico.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                                    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT, idade INTEGER, cep TEXT, email TEXT, cpf TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cursos (
                                    curso_id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (
                                    turma_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT, curso_id INTEGER, turno TEXT,
                                    FOREIGN KEY(curso_id) REFERENCES cursos(curso_id))''')
        self.conn.commit()

    def execute_query(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        self.conn.commit()

    def fetch_data(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()
