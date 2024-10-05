import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas.

# Função que adiciona o texto do botão pressionado à expressão
def click_button(item):
    global expression
    expression += str(item)  # Concatena o valor do botão à expressão atual
    input_text.set(expression)  # Atualiza o campo de entrada com a nova expressão

# Função para calcular o resultado da expressão
def evaluate():
    try:
        global expression
        result = str(eval(expression))  # Calcula a expressão usando a função eval
        input_text.set(result)  # Exibe o resultado no campo de entrada
        expression = ""  # Reseta a expressão após o cálculo
    except:
        input_text.set("Error")  # Exibe "Error" caso ocorra um erro (como divisão por zero)
        expression = ""  # Limpa a expressão

# Função que limpa o campo de entrada e a expressão
def clear():
    global expression
    expression = ""  # Reseta a variável de expressão
    input_text.set("")  # Limpa o campo de entrada

# Configuração da janela principal (root)
root = tk.Tk()  # Cria uma instância da janela principal
root.title("Calculadora")  # Define o título da janela
root.geometry("300x400")  # Define o tamanho da janela
root.resizable(False, False)  # Impede que a janela seja redimensionada

# Variável que armazena a expressão a ser calculada
expression = ""
input_text = tk.StringVar()  # Cria uma variável para armazenar o texto exibido no campo de entrada

# Frame que contém o campo de entrada da calculadora
input_frame = tk.Frame(root, width=312, height=50, bd=0, 
                       highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)  # Coloca o frame no topo da janela

# Campo de entrada onde a expressão e o resultado serão exibidos
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, 
                       width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)  # Define a posição do campo de entrada dentro do grid
input_field.pack(ipady=10)  # Ajusta o padding interno do campo de entrada

# Frame onde os botões da calculadora serão colocados
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()  # Coloca o frame de botões abaixo do campo de entrada

# Lista de botões com suas respectivas funções: (texto do botão, quantas colunas ocupa, função ao clicar)
buttons = [
    ('C', 3, lambda: clear()),  # Botão de limpar ocupa 3 colunas
    ('/', 1, lambda: click_button('/')),  # Botão de divisão
    ('7', 1, lambda: click_button(7)),  # Botão do número 7
    ('8', 1, lambda: click_button(8)),  # Botão do número 8
    ('9', 1, lambda: click_button(9)),  # Botão do número 9
    ('X', 1, lambda: click_button('*')),  # Botão de multiplicação
    ('4', 1, lambda: click_button(4)),  # Botão do número 4
    ('5', 1, lambda: click_button(5)),  # Botão do número 5
    ('6', 1, lambda: click_button(6)),  # Botão do número 6
    ('-', 1, lambda: click_button('-')),  # Botão de subtração
    ('1', 1, lambda: click_button(1)),  # Botão do número 1
    ('2', 1, lambda: click_button(2)),  # Botão do número 2
    ('3', 1, lambda: click_button(3)),  # Botão do número 3
    ('+', 1, lambda: click_button('+')),  # Botão de adição
    ('0', 2, lambda: click_button(0)),  # Botão do número 0, ocupa 2 colunas
    ('.', 1, lambda: click_button('.')),  # Botão de ponto decimal
    ('=', 1, lambda: evaluate())  # Botão de igual para calcular a expressão
]

# Variáveis para rastrear a linha e coluna do grid
row_val = 0  # Começa na linha 0
col_val = 0  # Começa na coluna 0

# Loop para criar os botões dinamicamente
for text, col_span, command in buttons:
    # Cria cada botão usando as informações da lista (texto, colunas, comando)
    tk.Button(btns_frame, text=text, fg="black", width=10 * col_span, height=3, bd=0,
              bg="#ffa500" if text in ['/', 'X', '-', '+', '='] else "#eee" if text == 'C' else "#fff",
              cursor="hand2", command=command).grid(row=row_val, column=col_val, columnspan=col_span, padx=1, pady=1)
    
    col_val += col_span  # Atualiza a coluna de acordo com o espaço que o botão ocupa
    if col_val > 3:  # Se passar de 3 colunas, vai para a próxima linha
        col_val = 0
        row_val += 1  # Muda para a próxima linha

# Inicia o loop principal da aplicação para manter a interface em execução
root.mainloop()