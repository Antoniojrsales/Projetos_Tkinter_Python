from tkinter import *

janela = Tk()
janela.title('Somando dois numeros')
janela.geometry('300x250')
janela.config(bg='light gray')
janela.resizable(width=False, height=False)

def limpar_texto():
    entradaum.delete(0, END)
    entradadois.delete(0, END)
    resultfinal['text'] = ''

def somar_tudo():
    resultfinal['text'] = int(entradaum.get()) + int(entradadois.get())
      

valor_texto = StringVar
label_valorum = Label(janela, width=6, height=1, 
               text='1 Valor: ', font='Arial 15 bold', padx=7, bg='light gray', justify=RIGHT)
label_valorum.grid(row=0, column=0, pady=2)
entradaum = Entry(janela, width=12, 
               text='', font='Arial 15 bold', relief=FLAT, justify=RIGHT)
entradaum.grid(row=0, column=1, pady=2)

label_valordois = Label(janela, width=6, height=1, 
               text='2 Valor: ', font='Arial 15 bold', padx=7, bg='light gray', justify=RIGHT)
label_valordois.grid(row=1, column=0, pady=2)
entradadois = Entry(janela, width=12, 
               text='', font='Arial 15 bold', relief=FLAT, justify=RIGHT)
entradadois.grid(row=1, column=1, pady=2)

labelresult = Label(janela, width=6, height=1, 
               text='Result: ', font='Arial 15 bold', bg='light gray')
labelresult.grid(row=2, column=0, pady=2)

resultfinal = Label(janela, text='', width=10, font='Arial 15 bold', relief=FLAT, padx=7, 
                anchor=CENTER, justify=RIGHT)
resultfinal.grid(row=2, column=1, pady=2)

botao_igual = Button(janela, command=somar_tudo, width=8, text='Resultado', font='Arial 15 bold', 
                     relief=SOLID, bg='blue', fg='white')
botao_igual.grid(row=3, column=0, pady=2)

botao_limpar = Button(janela, command=limpar_texto, width=8, text='C', font='Arial 15 bold', 
                      relief=SOLID, bg='green', fg='white')
botao_limpar.grid(row=4, column=0, pady=2)


janela.mainloop()