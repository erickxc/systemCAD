class Cadastrar:
    def __init__(self, db):
        self.db = db

    def cadastrar_aluno(self, aluno):
        query = "INSERT INTO alunos (nome, idade, cep, email, cpf) VALUES (?, ?, ?, ?, ?)"
        self.db.execute_query(query, (aluno.nome, aluno.idade, aluno.cep, aluno.email, aluno.cpf))

    def cadastrar_curso(self, curso):
        query = "INSERT INTO cursos (nome) VALUES (?)"
        self.db.execute_query(query, (curso.nome,))

    def cadastrar_turma(self, turma):
        query = "INSERT INTO turmas (nome, curso_id, turno) VALUES (?, ?, ?)"
        self.db.execute_query(query, (turma.nome, turma.curso_id, turma.turno))
