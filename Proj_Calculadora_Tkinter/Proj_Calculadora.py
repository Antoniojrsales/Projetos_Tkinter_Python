#Bibliotecas
from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#3b3b3b'
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#ECEFF1'
cor5 = '#FFAB40'

#Config janela principal
janela = Tk()
janela.title('Calculadora')
janela.geometry('322x313')
janela.config(background='white')
janela.resizable(False, False)
janela.iconphoto(False, PhotoImage(file='icon.png'))

#Dividindo a janela em dois frames
frame_tela = Frame(janela, width=322, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_botao = Frame(janela, width=322, height=313)
frame_botao.grid(row=1, column=0)

todos_valores = ''
todos_operadores = ''

def entrar_operadores(event):
    global todos_operadores
    todos_operadores = str(event)      
    valor_texto.set(todos_operadores)

def entrar_valores(event):
    global todos_valores
    todos_valores += str(event)      
    valor_texto.set(todos_valores)

valor_texto = StringVar()

#Criando uma label
lb_entrada = Label(frame_tela, textvariable=valor_texto, bg=cor3, fg=cor2, font='Arial 15', width=28, height=2, padx=7, relief=FLAT,
                   anchor='e', justify=RIGHT)
lb_entrada.grid(row=0, column=0, columnspan=10)

#Criando os botoes
botao_c = Button(frame_botao, text='C', width=15, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_c.place(x=1, y=0)
botao_porc = Button(frame_botao, text='%' , command=lambda:entrar_operadores('%'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_porc.place(x=161, y=0)
botao_div = Button(frame_botao, text='/' , command=lambda:entrar_operadores('/'), width=7, height=2, bg=cor5, fg=cor2, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_div.place(x=241, y=0)

botao_sete = Button(frame_botao, text='7' , command=lambda:entrar_valores('7'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_sete.place(x=0, y=52)
botao_oito = Button(frame_botao, text='8' , command=lambda:entrar_valores('8'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_oito.place(x=80, y=52)
botao_nove = Button(frame_botao, text='9' , command=lambda:entrar_valores('9'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_nove.place(x=161, y=52)
botao_mult = Button(frame_botao, text='*' , command=lambda:entrar_operadores('*'), width=7, height=2, bg=cor5, fg=cor2, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_mult.place(x=241, y=52)

botao_quatro = Button(frame_botao, text='4' , command=lambda:entrar_valores('4'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_quatro.place(x=0, y=104)
botao_cinco = Button(frame_botao, text='5' , command=lambda:entrar_valores('5'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_cinco.place(x=80, y=104)
botao_seis = Button(frame_botao, text='6' , command=lambda:entrar_valores('6'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_seis.place(x=161, y=104)
botao_menos = Button(frame_botao, text='-' , command=lambda:entrar_operadores('-'), width=7, height=2, bg=cor5, fg=cor2, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_menos.place(x=241, y=104)

botao_um = Button(frame_botao, text='1' , command=lambda:entrar_valores('1'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_um.place(x=0, y=156)
botao_dois = Button(frame_botao, text='2' , command=lambda:entrar_valores('2'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_dois.place(x=80, y=156)
botao_tres = Button(frame_botao, text='3' , command=lambda:entrar_valores('3'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_tres.place(x=161, y=156)
botao_mais = Button(frame_botao, text='+' , command=lambda:entrar_operadores('+'), width=7, height=2, bg=cor5, fg=cor2, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_mais.place(x=241, y=156)

botao_zero = Button(frame_botao, text='0' , command=lambda:entrar_valores('0'), width=15, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_zero.place(x=0, y=208)
botao_ponto = Button(frame_botao, text='.' , command=lambda:entrar_operadores('.'), width=7, height=2, bg=cor4, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_ponto.place(x=161, y=208)
botao_igual = Button(frame_botao, text='=', width=7, height=2, bg=cor5, fg=cor2, font=('Arial 13 bold'), 
                 relief=RAISED, overrelief=RIDGE)
botao_igual.place(x=241, y=208)



janela.mainloop()