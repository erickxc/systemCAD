class Listar:
    def __init__(self, db):
        self.db = db

    def listar_alunos(self):
        query = "SELECT * FROM alunos"
        return self.db.fetch_data(query)

    def listar_cursos(self):
        query = "SELECT * FROM cursos"
        return self.db.fetch_data(query)

    def listar_turmas(self):
        query = "SELECT * FROM turmas"
        return self.db.fetch_data(query)
