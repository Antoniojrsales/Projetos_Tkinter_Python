from tkinter import *

# Criação da janela principal
janela_tabuada = Tk()
janela_tabuada.title('Tabuada')  # Define o título da janela
janela_tabuada.geometry('300x400')  # Define o tamanho inicial da janela
janela_tabuada.config(bg='light gray')  # Define a cor de fundo da janela
janela_tabuada.resizable(True, True)  # Permite redimensionar a janela

# Função para limpar a entrada e o resultado
def limpar_texto():
    entrada_label.delete(0, END)  # Limpa o campo de entrada
    label_erro['text'] = ''  # Limpa o texto de erro
    label_resultado['text'] = ''  # Limpa o resultado da tabuada

# Função para calcular a tabuada
def botao_calcular():
    try:
        entrada = int(entrada_label.get())  # Tenta converter o valor de entrada para inteiro
        resultado = ''  # Inicializa uma string vazia para armazenar o resultado
        
        # Calcula a tabuada do número digitado
        for contador in range(1, 11):
            resultado += f'{entrada} X {contador} = {entrada * contador}\n'  # Concatena o resultado de cada linha na string
        
        label_resultado['text'] = resultado  # Atualiza o label com o resultado calculado
        label_erro['text'] = ''  # Limpa o texto de erro, se existir
    except ValueError:
        # Exibe uma mensagem de erro se o valor de entrada não for um número válido
        label_erro['text'] = 'Favor digitar um valor válido'
        label_resultado['text'] = ''  # Limpa o resultado anterior

# Criação de widgets (componentes da interface)

# Frame para organizar os elementos na parte superior
frame_top = Frame(janela_tabuada, bg='light gray', pady=10)
frame_top.pack(fill=X)

# Label de instrução para o usuário
label = Label(frame_top, width=12, height=1, text='Digite um valor:', bg='light gray', fg='black',
              font=('Ivy 15'), padx=7, relief=FLAT, anchor='e', justify=RIGHT)
label.pack()

# Campo de entrada para o usuário digitar o número
entrada_label = Entry(frame_top, width=12, font=('Ivy 12 bold'), relief=FLAT, justify=RIGHT)
entrada_label.pack(pady=5)

# Frame para organizar os botões
frame_buttons = Frame(janela_tabuada, bg='light gray')
frame_buttons.pack(pady=10)

# Botão para calcular a tabuada
buton_somar = Button(frame_buttons, width=12, command=botao_calcular, text='Calcular', font=('Ivy 12 bold'),
                     bg='blue', fg='White', relief=FLAT)
buton_somar.grid(row=0, column=0, padx=5)

# Botão para limpar a entrada e o resultado
botao_limpar = Button(frame_buttons, command=limpar_texto, width=8, text='C', font='Ivy 12 bold',
                      relief=FLAT, bg='green', fg='white')
botao_limpar.grid(row=0, column=1, padx=5)

# Frame para o resultado
frame_resultado = Frame(janela_tabuada, bg='light gray', pady=10)
frame_resultado.pack(fill=BOTH, expand=True)

# Label para exibir o resultado da tabuada
label_resultado = Label(frame_resultado, text='', font='Ivy 12 bold', bg='light gray', justify=LEFT, anchor='nw')
label_resultado.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Label para exibir erros de entrada
label_erro = Label(janela_tabuada, text='', font='Ivy 10 bold', bg='light gray')
label_erro.pack()

# Inicia o loop principal da janela
janela_tabuada.mainloop()