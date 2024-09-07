#Biblioteca#
from tkinter import *

#Criando a Janela no Tkinter#
janela = Tk()
janela.title('Calculadora IMC')
janela.geometry('480x320+200+200')
janela.config(bg='light gray')
janela.resizable(width=False, height=False)

#Funcao para Limpar os dados digitados#
def limpar_texto():
    entrada_peso.delete(0, END)
    entrada_altura.delete(0, END)
    lb_imc['text'] = ''
    lb_status['text'] = ''

#Funcao para calcular o IMC e qual o status do IMC#
def calcular_imc():    
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        resultado = peso / (altura ** 2)
        lb_imc['text'] = f'{resultado:.2f}'
        
        if altura > 2.1:
            lb_imc['text'] = ''
            lb_status['text'] = 'Altura indisponivel favor digitar novamente'
        elif resultado < 18.5:
            lb_status['text'] = 'O seu imc esta: Abaixo do Peso'
        elif resultado <= 24.9:
            lb_status['text'] = 'O seu imc esta: Peso Ideal'
        elif resultado <= 29.9:
            lb_status['text'] = 'O seu imc esta: Levemente acima do Peso'
        elif resultado <= 34.9:
            lb_status['text'] = 'O seu imc esta: Obesidade Grau 1'
        elif resultado <= 39.9:
            lb_status['text'] = 'O seu imc esta: Obesidade Grau 2'
        else:
            lb_status['text'] = 'O seu imc esta: Obesidade Morbida'
    except ValueError:
        lb_status['text'] = 'Valores invalidos favor digitar novamente'

#Criando as Labels os Botoes e as Caixas de entradas#
lb_nome = Label(janela, text='Calculadora de IMC', bg='light gray', width=20, font='Ivy 17 bold', anchor='center')
lb_nome.place(x=100, y=20)

lb_linha = Label(janela, bg='#D2F7FF', width=80, height=1)
lb_linha.place(x=5, y=60)

lb_status = Label(janela, text='', bg='light gray', width=40, font='Ivy 16')
lb_status.place(x=10, y=220)

lb_imc = Label(janela, text='', bg='#D2F7FF', fg='#000099', width=9, height=3, font='Ivy 18 bold')
lb_imc.place(x=320, y=108)

lb_peso = Label(janela, text='Insira o seu Peso', bg='light gray', width=20, font='Ivy 12 bold')
lb_peso.place(x=0, y=120)
entrada_peso = Entry(janela, width=8, font='Ivy 14 bold', relief=RAISED, justify=RIGHT)
entrada_peso.place(x=180, y=122)

lb_altura = Label(janela, text='Insira o sua Altura', bg='light gray', width=20, font='Ivy 12 bold')
lb_altura.place(x=0, y=170)
entrada_altura = Entry(janela, width=8, font='Ivy 14 bold', relief=RAISED, justify=RIGHT)
entrada_altura.place(x=180, y=172)

botao = Button(janela, command=calcular_imc, text='Calcular', bg='blue', fg='white', width=15, height=1, font='Ivy 14 bold')
botao.place(x=20, y=265)

botao_limpar = Button(janela, command=limpar_texto, text='C', bg='green', fg='white', width=8, font='Ivy 14 bold')
botao_limpar.place(x=220, y=265)

janela.mainloop()



