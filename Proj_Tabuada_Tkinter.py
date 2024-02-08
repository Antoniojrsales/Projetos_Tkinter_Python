from tkinter import *

janela_tabuada = Tk()
janela_tabuada.title('Tabuada')
janela_tabuada.geometry('300x260+500+300')
janela_tabuada.config(bg='light gray')

def limpar_texto():
    entrada_label.delete(0, END)
    label_erro['text'] = ''
        
def botao_calcular():
    try:
        entrada = int(entrada_label.get())
        for contador in range(1, 11):           
            label_saida = Label(janela_tabuada, text=f'{entrada} X {contador} = {entrada * contador}',
                                 font=('Ivy 12 bold'), bg='light gray', fg='black').pack(anchor=E)
    except ValueError:
        label_erro['text'] = 'Favor digitar um valor valido'

label = Label(janela_tabuada, width=12, height=1, text='Digite um valor: ',bg='light gray', fg='black',
                      font=('Ivy 15'), padx=7, relief=FLAT, anchor='e', justify=RIGHT)
label.place(x=10, y=10)

entrada_label = Entry(janela_tabuada, width=12, font=('Ivy 12 bold'), relief=FLAT, justify=RIGHT)
entrada_label.place(x=30, y=40)

buton_somar = Button(janela_tabuada,width=12, command=botao_calcular, text='Calcular', font=('Ivy 12 bold'),
                      bg='blue', fg='White')
buton_somar.place(x=20, y=70)

botao_limpar = Button(janela_tabuada, command=limpar_texto, width=8, text='C', font='Ivy 15 bold', 
                      relief=SOLID, bg='green', fg='white')
botao_limpar.place(x=20, y=110)

label_erro = Label(janela_tabuada, text='', font='Ivy 10 bold', bg='light gray')
label_erro.place(x=10, y=200)

janela_tabuada.mainloop()