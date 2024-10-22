from database import Database

class Turma:
    def cadastrar(self, nome, curso_id, turno):
        db = Database()
        db.execute("INSERT INTO turmas (nome, curso_id, turno) VALUES (?, ?, ?)", (nome, curso_id, turno))
        db.commit()
        db.close()

    def listar(self, tabela):
        db = Database()
        db.execute("SELECT * FROM turmas")
        for row in db.cursor.fetchall():
            tabela.insert("", tk.END, values=row)
        db.close()

    def excluir(self, turma_id):
        db = Database()
        db.execute("DELETE FROM turmas WHERE turma_id=?", (turma_id,))
        db.commit()
        db.close()
