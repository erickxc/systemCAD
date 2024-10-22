from database import Database

class Curso:
    def cadastrar(self, nome):
        db = Database()
        db.execute("INSERT INTO cursos (nome) VALUES (?)", (nome,))
        db.commit()
        db.close()

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
