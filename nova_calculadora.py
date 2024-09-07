#Biblioteca#
from tkinter import *

#Criando uma janela#
screen = Tk()
screen.title('Nova Calculadora Tkinter')
screen.resizable(False,False)
btns = []
todos_valores = ''

def print_label(texto):
    widget_entrada.config(text=texto)

def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def limpar_tudo():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

valor_texto = StringVar()

#Criando o laco dos botoes#
for i in range(11):
    botao_aux = Button(screen, text=i, width=8, bg='yellow',font='Ivy 17',
                       command=lambda x=i: print_label(x))
    btns.append(botao_aux)

#Criando uma janela de entradade caracter#
widget_entrada = Label(screen, textvariable=valor_texto, width=33, height=3, bg='gray', font='Ivy 17', 
                       padx=7, relief=FLAT, anchor='e', justify=RIGHT)
widget_entrada.grid(row=0, column=0, columnspan=10)

#criando os botoes#
btns[7].grid(row=2, column=1)
btns[8].grid(row=2, column=2)
btns[9].grid(row=2, column=3)
btns_menos = Button(screen, text="-", command=lambda:entrar_valores('-'), width=8, bg='red', font=('Ivy 17'))
btns_menos.grid(row=2, column=4)

btns[4].grid(row=3, column=1)
btns[5].grid(row=3, column=2)
btns[6].grid(row=3, column=3)
btns_mais = Button(screen, text="+", width=8, bg='red', font=('Ivy 17'))
btns_mais.grid(row=3, column=4)

btns[1].grid(row=4, column=1)
btns[2].grid(row=4, column=2)
btns[3].grid(row=4, column=3)
btns_dividir = Button(screen, text="/", width=8, bg='red', font=('Ivy 17'))
btns_dividir.grid(row=4, column=4)

btns_limpar = Button(screen, command=lambda:limpar_tudo(), text="C",width=8, bg='green', font=('Ivy 17'))
btns_limpar.grid(row=5, column=1)
btns[0].grid(row=5, column=2)
btns_igual = Button(screen, text="=",width=8, bg='red', font=('Ivy 17'))
btns_igual.grid(row=5, column=3)
btns_multiplica = Button(screen, text="*",width=8, bg='red', font=('Ivy 17'))
btns_multiplica.grid(row=5, column=4)

screen.mainloop()

