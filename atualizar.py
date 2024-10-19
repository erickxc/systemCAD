class Atualizar:
    def __init__(self, db):
        self.db = db

    def atualizar_aluno(self, matricula, aluno):
        query = "UPDATE alunos SET nome = ?, idade = ?, cep = ?, email = ?, cpf = ? WHERE matricula = ?"
        self.db.execute_query(query, (aluno.nome, aluno.idade, aluno.cep, aluno.email, aluno.cpf, matricula))

    def atualizar_curso(self, curso_id, curso):
        query = "UPDATE cursos SET nome = ? WHERE curso_id = ?"
        self.db.execute_query(query, (curso.nome, curso_id))

    def atualizar_turma(self, turma_id, turma):
        query = "UPDATE turmas SET nome = ?, curso_id = ?, turno = ? WHERE turma_id = ?"
        self.db.execute_query(query, (turma.nome, turma.curso_id, turma.turno, turma_id))
