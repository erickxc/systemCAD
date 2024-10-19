from database import Database
from models import Aluno, Curso, Turma
from cadastrar import Cadastrar
from listar import Listar
from excluir import Excluir
from atualizar import Atualizar

class SistemaAcademico:
    def __init__(self, db):
        self.db = db
        self.cadastrar = Cadastrar(db)
        self.listar = Listar(db)
        self.excluir = Excluir(db)
        self.atualizar = Atualizar(db)

# Inicializando o sistema acadêmico
if __name__ == "__main__":
    db = Database()
    sistema = SistemaAcademico(db)

    # Exemplo de cadastro de aluno
    aluno = Aluno("João Silva", 20, "12345-678", "joao@email.com", "123.456.789-00")
    sistema.cadastrar.cadastrar_aluno(aluno)

    # Listar alunos
    alunos = sistema.listar.listar_alunos()
    for aluno in alunos:
        print(aluno)

    # Atualizar aluno
    aluno_atualizado = Aluno("João Silva Atualizado", 21, "87654-321", "joao.novo@email.com", "987.654.321-00")
    sistema.atualizar.atualizar_aluno(1, aluno_atualizado)

    # Excluir aluno
    sistema.excluir.excluir_aluno(1)
