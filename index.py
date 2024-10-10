import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from colorama import Fore, Style, init

# Inicializando o colorama
init(autoreset=True)

def criar_tabelas():
    try:
        print('Criando tabelas...')
        conn = sqlite3.connect('tabelas.db')
        cursor = conn.cursor()

        # Tabela Alunos
        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                          matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT,
                          idade INTEGER,
                          cep TEXT,
                          email TEXT,
                          cpf TEXT)''')

        # Tabela Cursos
        cursor.execute('''CREATE TABLE IF NOT EXISTS cursos (
                          curso_id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT)''')

        # Tabela Turmas
        cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (
                          turma_id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT,
                          curso_id INTEGER,
                          turno TEXT,
                          FOREIGN KEY(curso_id) REFERENCES cursos(curso_id))''')

        # Tabela de relacionamento Alunos / Turmas
        cursor.execute('''CREATE TABLE IF NOT EXISTS alunos_turmas(
                          matricula INTEGER,
                          turma_id INTEGER,
                          FOREIGN KEY(matricula) REFERENCES alunos(matricula),
                          FOREIGN KEY(turma_id) REFERENCES turmas(turma_id))''')

        conn.commit()
        conn.close()
        print('Tabelas criadas com sucesso!')

    except sqlite3.Error as e:
        print(f"{Fore.RED}Erro ao criar a tabela: {e}")

# Funções para Alunos
def cadastrar_aluno():
    nome = nome_aluno_entry.get()
    idade = idade_aluno_entry.get()
    cep = cep_aluno_entry.get()
    email = email_aluno_entry.get()
    cpf = cpf_aluno_entry.get()

    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, cep, email, cpf) VALUES (?, ?, ?, ?, ?)",
                   (nome, idade, cep, email, cpf))

    conn.commit()
    conn.close()
    limpar_campos_aluno()

def limpar_campos_aluno():
    nome_aluno_entry.delete(0, tk.END)
    idade_aluno_entry.delete(0, tk.END)
    cep_aluno_entry.delete(0, tk.END)
    email_aluno_entry.delete(0, tk.END)
    cpf_aluno_entry.delete(0, tk.END)

def listar_alunos():
    try:
        for i in tabela_alunos.get_children():
            tabela_alunos.delete(i)

        conn = sqlite3.connect('tabelas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos")

        for row in cursor.fetchall():
            tabela_alunos.insert("", tk.END, values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao listar alunos: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()

# Função para abrir a tela de cadastro de alunos
def abrir_cadastro_alunos():
    print('Cadastrando aluno...')
    cadastro_alunos_window = tk.Toplevel(root)
    cadastro_alunos_window.title("Cadastro de Alunos")

    tk.Label(cadastro_alunos_window, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    global nome_aluno_entry
    nome_aluno_entry = tk.Entry(cadastro_alunos_window, width=40)
    nome_aluno_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(cadastro_alunos_window, text="Idade:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    global idade_aluno_entry
    idade_aluno_entry = tk.Entry(cadastro_alunos_window, width=40)
    idade_aluno_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(cadastro_alunos_window, text="CEP:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    global cep_aluno_entry
    cep_aluno_entry = tk.Entry(cadastro_alunos_window, width=40)
    cep_aluno_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(cadastro_alunos_window, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    global email_aluno_entry
    email_aluno_entry = tk.Entry(cadastro_alunos_window, width=40)
    email_aluno_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(cadastro_alunos_window, text="CPF:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    global cpf_aluno_entry
    cpf_aluno_entry = tk.Entry(cadastro_alunos_window, width=40)
    cpf_aluno_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Button(cadastro_alunos_window, text="Cadastrar Aluno", command=cadastrar_aluno).grid(row=5, column=1, pady=10)
    tk.Button(cadastro_alunos_window, text="Listar Alunos", command=listar_alunos).grid(row=5, column=0, pady=10)

    # Tabela para listar alunos
    global tabela_alunos
    tabela_alunos = ttk.Treeview(cadastro_alunos_window, columns=("Matrícula", "Nome", "Idade", "CEP", "Email", "CPF"),
                                   show='headings')
    tabela_alunos.heading("Matrícula", text="Matrícula")
    tabela_alunos.heading("Nome", text="Nome")
    tabela_alunos.heading("Idade", text="Idade")
    tabela_alunos.heading("CEP", text="CEP")
    tabela_alunos.heading("Email", text="Email")
    tabela_alunos.heading("CPF", text="CPF")
    tabela_alunos.grid(row=6, column=0, columnspan=2)  # A tabela ocupa a linha 6

    # Botão de voltar na linha 7
    tk.Button(cadastro_alunos_window, text="Voltar", command=cadastro_alunos_window.destroy).grid(row=7,column=0,columnspan=2, pady=10)

# Funções para Cursos
def cadastrar_curso():
    nome_curso = nome_curso_entry.get()

    if not nome_curso:
        messagebox.showwarning("Cadastrar Curso", "O nome do curso não pode estar vazio.")
        return

    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cursos (nome) VALUES (?)", (nome_curso,))
    conn.commit()
    conn.close()
    limpar_campos_curso()
    exibir_cursos()

def limpar_campos_curso():
    nome_curso_entry.delete(0, tk.END)

def exibir_cursos():
    for i in tabela_cursos.get_children():
        tabela_cursos.delete(i)
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos")
    for row in cursor.fetchall():
        tabela_cursos.insert("", tk.END, values=row)
    conn.close()

def atualizar_curso():
    selected_item = tabela_cursos.selection()[0]
    curso_id = tabela_cursos.item(selected_item)['values'][0]
    nome_curso = nome_curso_entry.get()

    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE cursos SET nome=? WHERE curso_id=?", (nome_curso, curso_id))
    conn.commit()
    conn.close()
    exibir_cursos()
    limpar_campos_curso()

def excluir_curso():
    selected_item = tabela_cursos.selection()[0]
    curso_id = tabela_cursos.item(selected_item)['values'][0]

    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cursos WHERE curso_id=?", (curso_id,))
    conn.commit()
    conn.close()
    exibir_cursos()

def abrir_cadastro_cursos():
    cadastro_cursos_window = tk.Toplevel(root)
    cadastro_cursos_window.title("Cadastro de Cursos")

    tk.Label(cadastro_cursos_window, text="Nome do Curso:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    global nome_curso_entry
    nome_curso_entry = tk.Entry(cadastro_cursos_window, width=40)
    nome_curso_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(cadastro_cursos_window, text="Cadastrar Curso", command=cadastrar_curso).grid(row=1, column=1, pady=10)
    tk.Button(cadastro_cursos_window, text="Listar Cursos", command=exibir_cursos).grid(row=1, column=0, pady=10)

    # Tabela de Cursos
    global tabela_cursos
    tabela_cursos = ttk.Treeview(cadastro_cursos_window, columns=("ID", "Nome"), show='headings')
    tabela_cursos.heading("ID", text="ID")
    tabela_cursos.heading("Nome", text="Nome")
    tabela_cursos.grid(row=2, column=0, columnspan=2)

    # Botões para atualizar e excluir
    tk.Button(cadastro_cursos_window, text="Atualizar Curso", command=atualizar_curso).grid(row=3, column=0, pady=10)
    tk.Button(cadastro_cursos_window, text="Excluir Curso", command=excluir_curso).grid(row=3, column=1, pady=10)

    # Botão de voltar na linha 4
    tk.Button(cadastro_cursos_window, text="Voltar", command=cadastro_cursos_window.destroy).grid(row=4,column=0,columnspan=2, pady=10)

# Funções para Turmas
def cadastrar_turma():
    nome_turma = nome_turma_entry.get()
    curso_id = curso_id_combobox.get()
    turno = turno_entry.get()

    if not nome_turma or not curso_id or not turno:
        messagebox.showwarning("Cadastrar Turma", "Preencha todos os campos.")
        return

    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turmas (nome, curso_id, turno) VALUES (?, ?, ?)", (nome_turma, curso_id, turno))
    conn.commit()
    conn.close()
    limpar_campos_turma()
    exibir_turmas()


def cadastrar_aluno_turma():
    matricula_aluno = matricula_aluno_combobox.get()
    turma_id = turma_id_combobox.get()

    if not matricula_aluno or not turma_id:
        messagebox.showwarning("Matricular Aluno na turma", "Selecione um aluno e uma turma.")
        return

    # Conectar ao banco de dados
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()

    # Inserir a associação de aluno e turma no banco de dados
    cursor.execute("INSERT INTO alunos_turmas (matricula, turma_id) VALUES (?, ?)", (matricula_aluno, turma_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Aluno matriculado com sucesso!")


# Função para abrir a tela de associação de aluno a turma
def abrir_associar_aluno_turma():
    associar_window = tk.Toplevel(root)
    associar_window.title("Associar Aluno a Turma")

    tk.Label(associar_window, text="Matrícula do Aluno:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    global matricula_aluno_combobox
    matricula_aluno_combobox = ttk.Combobox(associar_window, width=37)
    matricula_aluno_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Preencher o combobox com alunos cadastrados
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT matricula FROM alunos")
    alunos = cursor.fetchall()
    matricula_aluno_combobox['values'] = [aluno[0] for aluno in alunos]
    conn.close()

    tk.Label(associar_window, text="ID da Turma:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    global turma_id_combobox
    turma_id_combobox = ttk.Combobox(associar_window, width=37)
    turma_id_combobox.grid(row=1, column=1, padx=5, pady=5)

    # Preencher o combobox com turmas cadastradas
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT turma_id FROM turmas ")
    turmas = cursor.fetchall()
    turma_id_combobox['values'] = [turma[0] for turma in turmas]
    conn.close()

    # Botão para associar o aluno à turma
    tk.Button(associar_window, text="Associar", command=cadastrar_aluno_turma).grid(row=2, column=0, columnspan=2,
                                                                                    padx=5, pady=5)


def limpar_campos_turma():
    nome_turma_entry.delete(0, tk.END)
    curso_id_combobox.set("")
    turno_entry.delete(0, tk.END)

def exibir_turmas():
    for i in tabela_turmas.get_children():
        tabela_turmas.delete(i)
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turmas")
    for row in cursor.fetchall():
        tabela_turmas.insert("", tk.END, values=row)
    conn.close()

def abrir_cadastro_turmas():
    cadastro_turmas_window = tk.Toplevel(root)
    cadastro_turmas_window.title("Cadastro de Turmas")

    tk.Label(cadastro_turmas_window, text="Nome da Turma:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    global nome_turma_entry
    nome_turma_entry = tk.Entry(cadastro_turmas_window, width=40)
    nome_turma_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(cadastro_turmas_window, text="Curso ID:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    global curso_id_combobox
    curso_id_combobox = ttk.Combobox(cadastro_turmas_window, width=37)
    curso_id_combobox.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(cadastro_turmas_window, text="Turno:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    global turno_entry
    turno_entry = tk.Entry(cadastro_turmas_window, width=40)
    turno_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(cadastro_turmas_window, text="Cadastrar Turma", command=cadastrar_turma).grid(row=3, column=1, pady=10)
    tk.Button(cadastro_turmas_window, text="Listar Turmas", command=exibir_turmas).grid(row=3, column=0, pady=10)
    tk.Button(cadastro_turmas_window, text="Matricular Aluno em uma turma", command=abrir_associar_aluno_turma).grid(row=5, column=1, columnspan=2, pady=10)

    # Tabela de Turmas
    global tabela_turmas
    tabela_turmas = ttk.Treeview(cadastro_turmas_window, columns=("ID", "Nome", "Curso ID", "Turno"), show='headings')
    tabela_turmas.heading("ID", text="ID")
    tabela_turmas.heading("Nome", text="Nome")
    tabela_turmas.heading("Curso ID", text="Curso ID")
    tabela_turmas.heading("Turno", text="Turno")
    tabela_turmas.grid(row=4, column=0, columnspan=2)

    # Botão de voltar na linha 5
    tk.Button(cadastro_turmas_window, text="Voltar", command=cadastro_turmas_window.destroy).grid(row=5,column=0,columnspan=2, pady=10)

# Funções para Gerenciar Polo Acadêmico
def abrir_gerenciar_polo_academico():
    gerenciar_window = tk.Toplevel(root)
    gerenciar_window.title("Gerenciar Polo Acadêmico")


    # Criar um Treeview para exibir os dados
    global tabela_polo_academico
    tabela_polo_academico = ttk.Treeview(gerenciar_window, columns=("Matrícula", "Nome", "Turma", "Curso"), show='headings')
    tabela_polo_academico.heading("Matrícula", text="Matrícula")
    tabela_polo_academico.heading("Nome", text="Nome")
    tabela_polo_academico.heading("Turma", text="Turma")
    tabela_polo_academico.heading("Curso", text="Curso")

    # Usar grid para organizar o Treeview
    tabela_polo_academico.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Configurar a coluna para expansão
    gerenciar_window.grid_rowconfigure(0, weight=1)
    gerenciar_window.grid_columnconfigure(0, weight=1)

    # Adicionar dados ao Treeview
    conn = sqlite3.connect('tabelas.db')
    cursor = conn.cursor()

    # Executar a consulta
    cursor.execute('''
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

    # Inserir os resultados no Treeview
    for aluno in cursor.fetchall():
        tabela_polo_academico.insert("", "end", values=aluno)

    conn.close()

    # Botão de voltar
    tk.Button(gerenciar_window, text="Voltar", command=gerenciar_window.destroy).grid(row=1,column=0,columnspan=2, pady=10)

# Configurando a janela principal
root = tk.Tk()
root.title("Sistema Acadêmico")

# Botões do menu principal
tk.Button(root, text="Cadastrar Alunos", command=abrir_cadastro_alunos).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Cadastrar Cursos", command=abrir_cadastro_cursos).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Cadastrar Turmas", command=abrir_cadastro_turmas).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Gerenciar Polo Acadêmico", command=abrir_gerenciar_polo_academico).grid(row=1, column=1, padx=10, pady=10)

# Executando a função para criar as tabelas
criar_tabelas()

# Iniciando a interface gráfica
root.mainloop()
