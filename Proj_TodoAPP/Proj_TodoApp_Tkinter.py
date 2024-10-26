# Bibliotecas
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando a janela e suas configuracoes
root = tk.Tk()
root.title('ToDo App')
root.config(bg='#F0F0F0')
root.geometry('500x600')

# Variavel para armazenar o frame da tarefa que esta sendo editada
frame_em_edicao = None

# Funcao que adiciona as tarefas
def adicionar_tarefa():
    global frame_em_edicao
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != 'Escreva sua Tarefa aqui':
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            atualizar_tarefa(tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning('Entrada invalida, Por favor insira uma tarefa valida')

def ao_clicar_entrada():
    ...

def ao_sair_foco():
    ...

def atualizar_tarefa():
    ...

# Carregar icones
icon_edit = PhotoImage(file='editar.png').subsample(3, 3) # ajusta o icone conforme necessario
icon_delete = PhotoImage(file='deletar.png').subsample(3, 3) # ajusta o icone conforme necessario

# Criar uma fonte para o cabecalho
fonte_cabecalho = font.Font(family='Gamarond', size=24, weight='bold')

# Criar um rotulo do cabecalho
rotulo_cabecalho = tk.Label(root, text='Meu App de Tarefas', font=fonte_cabecalho, bg='#F0F0F0', fg='#333')
rotulo_cabecalho.pack(pady=20)

# Criando um frame na janela principal
frame = tk.Frame(root, bg='#F0F0F0')
frame.pack(pady=10)

# Coletando os dados da tarefa
entrada_tarefa = tk.Entry(frame, font=('Garamond', 14), relief=tk.FLAT, bg='white', fg='grey', width=30)
entrada_tarefa.insert(0, 'Escreva sua Tarefa aqui')
entrada_tarefa.bind('<FocusIn>', ao_clicar_entrada)
entrada_tarefa.bind('<FocusIn>', ao_sair_foco)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

# Criando o botao de adicionar Tarefa
botao_adicionar = tk.Button(frame, text='Adicionar Tarefa', command=adicionar_tarefa, bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto', 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)



root.mainloop()