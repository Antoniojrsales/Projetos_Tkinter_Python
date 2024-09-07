from tkinter import  *

janela = Tk()
janela.title("Calculadora_Tkinter")
janela.resizable(False,False)

todos_valores = ''

def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def limpar_valores():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

def calcular(event):
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    

# Criando widgets
valor_texto = StringVar()

widget_entrada = Label(janela, textvariable=valor_texto, width=30,height=3, bg='gray', font=('Ivy 17'), 
                       padx=7, relief=FLAT, anchor='e', justify=RIGHT)
widget_entrada.grid(row=0, column=0, columnspan=10)

widget1 = Button(janela, command= lambda:entrar_valores('7'), text="7", width=10, bg='yellow', font=('Ivy 13'))
widget1.grid(row=2, column=1)

widget2 = Button(janela, command= lambda:entrar_valores('8'), text="8", width=10, bg='yellow', font=('Ivy 13'))
widget2.grid(row=2, column=2)

widget3 = Button(janela, command= lambda:entrar_valores('9'), text="9", width=10, bg='yellow', font=('Ivy 13'))
widget3.grid(row=2, column=3)

widget4 = Button(janela, command= lambda:entrar_valores('-'), text="-", width=11, bg='red', font=('Ivy 13'))
widget4.grid(row=2, column=4)

widget5 = Button(janela, command= lambda:entrar_valores('4'), text="4", width=10, bg='yellow', font=('Ivy 13'))
widget5.grid(row=3, column=1)

widget6 = Button(janela, command= lambda:entrar_valores('5'), text="5", width=10, bg='yellow', font=('Ivy 13'))
widget6.grid(row=3, column=2)

widget7 = Button(janela, command= lambda:entrar_valores('6'), text="6", width=10, bg='yellow', font=('Ivy 13'))
widget7.grid(row=3, column=3)

widget8 = Button(janela, command= lambda:entrar_valores('+'),text="+", width=11, bg='red', font=('Ivy 13'))
widget8.grid(row=3, column=4)

widget9 = Button(janela, command= lambda:entrar_valores('1'), text="1", width=10, bg='yellow', font=('Ivy 13'))
widget9.grid(row=4, column=1)

widget10 = Button(janela, command= lambda:entrar_valores('2'), text="2",width=10, bg='yellow', font=('Ivy 13'))
widget10.grid(row=4, column=2)

widget11 = Button(janela, command= lambda:entrar_valores('3'), text="3",width=10, bg='yellow', font=('Ivy 13'))
widget11.grid(row=4, column=3)

widget12 = Button(janela, command= lambda:entrar_valores('/'),text="/",width=11, bg='red', font=('Ivy 13'))
widget12.grid(row=4, column=4)

widget13 = Button(janela, command= limpar_valores, text="C",width=10, bg='green', font=('Ivy 13'))
widget13.grid(row=5, column=1)

widget14 = Button(janela, command= lambda:entrar_valores('0'), text="0",width=10, bg='yellow', font=('Ivy 13'))
widget14.grid(row=5, column=2)

widget15 = Button(janela, command=lambda:calcular('='), text="=",width=10, bg='red', font=('Ivy 13'))
widget15.grid(row=5, column=3)

widget16 = Button(janela, command= lambda:entrar_valores('*'),text="*",width=11, bg='red', font=('Ivy 13'))
widget16.grid(row=5, column=4)

janela.mainloop()