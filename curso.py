from database import Database

class Curso:

    def __init__(self):
        self.db = Database()
        self.criar_tabela()

    def criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS cursos (
        curso_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        )
        """
        try:
            self.db.execute(query)
            print("Tabela 'cursos' criada com sucesso (ou já existe).")
        except Exception as e:
            print(f"Erro ao criar a tabela 'cursos': {e}")

    def cadastrar(self, nome):
        db = Database()
        try:
            db.execute("INSERT INTO cursos (nome) VALUES (?)", (nome,))
            db.commit()  # Confirma a operação
            print(f"Curso '{nome}' cadastrado com sucesso.")
        except Exception as e:
            print(f"Erro ao cadastrar o curso '{nome}': {e}")
        finally:
            db.close()  # Fecha a conexão com o banco de dados

    def listar(self, tabela):
        db = Database()
        db.execute("SELECT * FROM cursos")
        for row in db.cursor.fetchall():
            tabela.insert("", tk.END, values=row)
        db.close()

    def atualizar(self, curso_id, nome):
        db = Database()
        db.execute("UPDATE cursos SET nome=? WHERE curso_id=?", (nome, curso_id))
        db.commit()
        db.close()

    def excluir(self, curso_id):
        db = Database()
        db.execute("DELETE FROM cursos WHERE curso_id=?", (curso_id,))
        db.commit()
        db.close()
