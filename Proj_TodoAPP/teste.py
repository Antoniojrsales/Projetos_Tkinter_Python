# Importando as bibliotecas necessárias
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando a janela principal do aplicativo
window = tk.Tk()
window.title("Meu Todo App")
window.configure(bg="#f0f0f0")
window.geometry("500x600")

# Criando o cabeçalho da janela
source_header = font.Font(family="Garamond", size=24, weight="bold")  # Definindo a fonte e o estilo do cabeçalho
label_header = tk.Label(window, text="Todo App", font=source_header, bg="#F0F0F0", fg="#333")  # Criando o widget Label para o cabeçalho
label_header.pack(pady=20)

# Criando um espaço na janela para o campo de entrada e botão de adicionar tarefa
frame = tk.Frame(window, bg="#F0F0F0")  # Criando um Frame para agrupar widgets
frame.pack(pady=10)

# Criando um campo de entrada para o usuário adicionar tarefas
entry_task = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)  # Definindo o campo de entrada de texto
entry_task.pack(side=tk.LEFT, padx=10)

# Criando um botão para adicionar as tarefas
button_add = tk.Button(
    frame,
    text="Adicionar Tarefa",
    bg="#4CAF50",
    fg="white",
    height=1,
    width=15,
    font=("Roboto", 11),
    relief=tk.FLAT  # Estilo do botão (sem bordas elevadas)
)
button_add.pack(side=tk.LEFT, padx=10)

# Criando um espaço para a lista de tarefas
frame_list_task = tk.Frame(window, bg="white")
frame_list_task.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Adicionando o Frame ao layout para que ocupe todo o espaço disponível

# Criando um canvas para adicionar widgets com suporte para barra de rolagem
canvas = tk.Canvas(frame_list_task, bg="white")  # Canvas para a área de exibição de tarefas
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Posicionando o Canvas para preencher todo o espaço disponível

# Criando uma barra de rolagem vertical para a lista de tarefas
scrollbar = ttk.Scrollbar(frame_list_task, orient="vertical", command=canvas.yview)  # Barra de rolagem vinculada ao Canvas
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Posicionando a barra de rolagem à direita do Canvas

# Configurando o Canvas para utilizar a barra de rolagem
canvas.configure(yscrollcommand=scrollbar.set)  # Associando a barra de rolagem ao Canvas
canvas_interior = tk.Frame(canvas, bg="white")  # Criando um Frame dentro do Canvas para adicionar tarefas
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")  # Adicionando o Frame ao Canvas para que ele seja redimensionável

# Configurando o Canvas para redimensionar de acordo com o conteúdo
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))  # Atualizando a área de rolagem do Canvas quando o conteúdo muda

# Iniciando o loop principal da interface gráfica
window.mainloop()