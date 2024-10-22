from database import Database

class PoloAcademico:
    def listar(self, tabela):
        db = Database()
        db.execute('''
            SELECT 
                a.matricula, 
                a.nome AS aluno_nome, 
                t.nome AS turma_nome, 
                c.nome AS curso_nome
            FROM 
                alunos a
            JOIN 
                alunos_turmas at ON a.matricula = at.matricula
            JOIN 
                turmas t ON at.turma_id = t.turma_id
            JOIN 
                cursos c ON t.curso_id = c.curso_id
        ''')
        for row in db.cursor.fetchall():
            tabela.insert("", tk.END, values=row)
        db.close()
