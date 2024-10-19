class Aluno:
    def __init__(self, nome, idade, cep, email, cpf):
        self.nome = nome
        self.idade = idade
        self.cep = cep
        self.email = email
        self.cpf = cpf

class Curso:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome, curso_id, turno):
        self.nome = nome
        self.curso_id = curso_id
        self.turno = turno
