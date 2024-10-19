class Excluir:
    def __init__(self, db):
        self.db = db

    def excluir_aluno(self, matricula):
        query = "DELETE FROM alunos WHERE matricula = ?"
        self.db.execute_query(query, (matricula,))

    def excluir_curso(self, curso_id):
        query = "DELETE FROM cursos WHERE curso_id = ?"
        self.db.execute_query(query, (curso_id,))

    def excluir_turma(self, turma_id):
        query = "DELETE FROM turmas WHERE turma_id = ?"
        self.db.execute_query(query, (turma_id,))
