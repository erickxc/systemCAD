import tkinter as tk
from tkinter import messagebox
import cadastrar
import listar
import atualizar
import excluir

# Funções de interação com o sistema
def cadastrar_dados():
    cadastrar.main()

def listar_dados():
    listar.main()

def atualizar_dados():
    atualizar.main()

def excluir_dados():
    excluir.main()

# Criar a interface gráfica principal
def criar_interface():
    root = tk.Tk()
    root.title("Sistema Acadêmico - Interface Gráfica")

    # Tamanho da janela
    root.geometry("400x300")

    # Título
    label = tk.Label(root, text="Bem-vindo ao Sistema Acadêmico", font=("Arial", 16))
    label.pack(pady=20)

    # Botões para as funcionalidades
    btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_dados, width=20, height=2)
    btn_cadastrar.pack(pady=10)

    btn_listar = tk.Button(root, text="Listar", command=listar_dados, width=20, height=2)
    btn_listar.pack(pady=10)

    btn_atualizar = tk.Button(root, text="Atualizar", command=atualizar_dados, width=20, height=2)
    btn_atualizar.pack(pady=10)

    btn_excluir = tk.Button(root, text="Excluir", command=excluir_dados, width=20, height=2)
    btn_excluir.pack(pady=10)

    # Rodar a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    criar_interface()
