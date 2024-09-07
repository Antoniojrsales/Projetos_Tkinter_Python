from tkinter import *

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora Tkinter")  # Define o título da janela
janela.resizable(True, True)  # Permite o redimensionamento da janela

# Variável global para armazenar todos os valores digitados
todos_valores = ''

# Função para adicionar valores ao visor
def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)  # Adiciona o valor ao string de valores
    valor_texto.set(todos_valores)  # Atualiza o visor com o valor atual

# Função para limpar o visor
def limpar_valores():
    global todos_valores
    todos_valores = ''  # Limpa o string de valores
    valor_texto.set('')  # Atualiza o visor para vazio

# Função para calcular o resultado
def calcular():
    global todos_valores
    try:
        # Avalia a expressão aritmética usando a função eval
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))  # Atualiza o visor com o resultado
        todos_valores = str(resultado)  # Armazena o resultado para cálculos subsequentes
    except Exception as e:
        valor_texto.set("Erro")  # Mostra "Erro" em caso de entrada inválida
        todos_valores = ''  # Reseta a expressão

# Criando widgets
valor_texto = StringVar()  # Variável para armazenar o texto a ser exibido no visor

# Visor da calculadora
widget_entrada = Label(janela, textvariable=valor_texto, bg='gray', font=('Ivy 17'), 
                       padx=7, relief=FLAT, anchor='e', justify=RIGHT)
widget_entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")  # O argumento sticky permite o redimensionamento

# Configurando o redimensionamento para as linhas e colunas
janela.grid_rowconfigure(0, weight=1)  # Permite o redimensionamento do visor
for i in range(1, 6):  # Configura o redimensionamento das linhas de botões
    janela.grid_rowconfigure(i, weight=1)
    janela.grid_columnconfigure(i-1, weight=1)  # Configura o redimensionamento das colunas de botões

# Botões da calculadora
botoes = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('/', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('*', 5, 3)
]

# Criação dos botões dinamicamente
for (texto, linha, coluna) in botoes:
    if texto == 'C':
        btn = Button(janela, command=limpar_valores, text=texto, bg='green', font=('Ivy 13'))
    elif texto == '=':
        btn = Button(janela, command=calcular, text=texto, bg='red', font=('Ivy 13'))
    else:
        btn = Button(janela, command=lambda txt=texto: entrar_valores(txt), text=texto,
                     bg='yellow' if texto.isdigit() else 'red', font=('Ivy 13'))
    btn.grid(row=linha, column=coluna, sticky="nsew")  # O argumento sticky permite o redimensionamento

# Inicia o loop principal da interface gráfica
janela.mainloop()