import tkinter as tk
from tkinter import ttk
from aluno import Aluno
from curso import Curso
from turma import Turma

# Interface para Alunos
class InterfaceAluno:
    def __init__(self, root):
        self.aluno = Aluno()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Alunos")

        tk.Label(cadastro_window, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Idade:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        idade_entry = tk.Entry(cadastro_window, width=40)
        idade_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="CEP:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        cep_entry = tk.Entry(cadastro_window, width=40)
        cep_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        email_entry = tk.Entry(cadastro_window, width=40)
        email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="CPF:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        cpf_entry = tk.Entry(cadastro_window, width=40)
        cpf_entry.grid(row=4, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            idade = idade_entry.get()
            cep = cep_entry.get()
            email = email_entry.get()
            cpf = cpf_entry.get()
            self.aluno.cadastrar(nome, idade, cep, email, cpf)
            limpar_campos_aluno()
            listar()

        def limpar_campos_aluno():
            nome_entry.delete(0, tk.END)
            idade_entry.delete(0, tk.END)
            cep_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)

        tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).grid(row=5, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Matrícula", "Nome", "Idade", "CEP", "Email", "CPF"), show='headings')
        tabela.heading("Matrícula", text="Matrícula")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Idade", text="Idade")
        tabela.heading("CEP", text="CEP")
        tabela.heading("Email", text="Email")
        tabela.heading("CPF", text="CPF")
        tabela.grid(row=6, column=0, columnspan=2)

        def listar():
            self.aluno.listar(tabela)

        tk.Button(cadastro_window, text="Listar Alunos", command=listar).grid(row=5, column=0, pady=10)
        tk.Button(cadastro_window, text="Excluir Aluno", command=lambda: self.excluir_aluno(tabela)).grid(row=7, column=0, pady=10)
        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=7, column=1, pady=10)

    def excluir_aluno(self, tabela):
        try:
            selecionado = tabela.selection()[0]
            matricula = tabela.item(selecionado)['values'][0]
            self.aluno.excluir(matricula)
            self.aluno.listar(tabela)
        except IndexError:
            tk.messagebox.showerror("Erro", "Selecione um aluno para excluir.")


# Interface para Cursos
class InterfaceCurso:
    def __init__(self, root):
        self.curso = Curso()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Cursos")

        tk.Label(cadastro_window, text="Nome do Curso:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            self.curso.cadastrar(nome)

        tk.Button(cadastro_window, text="Cadastrar Curso", command=cadastrar).grid(row=1, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Curso_ID", "Nome"), show='headings')
        tabela.heading("Curso_ID", text="ID")
        tabela.heading("Nome", text="Nome")
        tabela.grid(row=2, column=0, columnspan=2)

        def listar():
            self.curso.listar(tabela)

        tk.Button(cadastro_window, text="Listar Cursos", command=listar).grid(row=3, column=0, pady=10)
        tk.Button(cadastro_window, text="Excluir Curso", command=lambda: self.curso.excluir(tabela.selection()[0])).grid(row=3, column=1, pady=10)

        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=4, column=1, pady=10)


# Interface para Turmas
class InterfaceTurma:
    def __init__(self, root):
        self.turma = Turma()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Turmas")

        tk.Label(cadastro_window, text="Nome da Turma:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Curso ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        curso_id_entry = tk.Entry(cadastro_window, width=40)
        curso_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Turno:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        turno_entry = tk.Entry(cadastro_window, width=40)
        turno_entry.grid(row=2, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            curso_id = curso_id_entry.get()
            turno = turno_entry.get()
            self.turma.cadastrar(nome, curso_id, turno)

        tk.Button(cadastro_window, text="Cadastrar Turma", command=cadastrar).grid(row=3, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Turma_ID", "Nome", "Curso_ID", "Turno"), show='headings')
        tabela.heading("Turma_ID", text="ID")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Curso_ID", text="Curso ID")
        tabela.heading("Turno", text="Turno")
        tabela.grid(row=4, column=0, columnspan=2)

        def listar():
            self.turma.listar(tabela)

        tk.Button(cadastro_window, text="Listar Turmas", command=listar).grid(row=5, column=0, pady=10)
        tk.Button(cadastro_window, text="Excluir Turma", command=lambda: self.turma.excluir(tabela.selection()[0])).grid(row=5, column=1, pady=10)

        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=6, column=1, pady=10)


# Janela principal
root = tk.Tk()
root.title("Sistema Acadêmico")

interface_aluno = InterfaceAluno(root)
interface_curso = InterfaceCurso(root)
interface_turma = InterfaceTurma(root)

tk.Button(root, text="Alunos", command=interface_aluno.abrir_cadastro).pack(padx=10, pady=10)
tk.Button(root, text="Cursos", command=interface_curso.abrir_cadastro).pack(padx=10, pady=10)
tk.Button(root, text="Turmas", command=interface_turma.abrir_cadastro).pack(padx=10, pady=10)

root.mainloop()
