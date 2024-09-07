from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

#------Cores------#
cor_b = '#f0f3f5'
cor_w = '#feffff'
cor_r = '#3fb5a3'
cor_v = '#38576b'
cor_lt = '#403d3d'

#--Criando a Janela e suas configuracoes--#
janela = Tk()
janela.title('Login')
janela.geometry('600x400')
janela.configure(background=cor_w)
janela.resizable(width=False, height=False)

#--Dividindo a Janela com Frame--#
frame_image = Frame(janela, width=200, height=400, bg=cor_w, relief='flat')
frame_image.grid(row=0, column=0, pady=1, padx=0)

frame_login = Frame(janela, width=200, height=400, bg=cor_w, relief='flat')
frame_login.grid(row=0, column=1, pady=1, padx=0)

#--Colocando uma imagem no Frame_image--#
img = ImageTk.PhotoImage(Image.open("login.jpg"))
painel = Label(frame_image, image = img, width=300, height=300)
painel.grid(row=1, column=0, padx=1, pady=0)

#--Criando uma label dentro do Frame_image--#
label_image = Label(frame_image, text='Faca o seu Login ou Cadastre-se\n na nossa plataforma para acessar\n nossos servicos', 
                    anchor=NE, font=('Ivy 11 bold'), bg=cor_b, fg=cor_lt)
label_image.grid(row=0, column=0, padx=1, pady=0)

#--Criando uma label dentro do Frame_login--#
label_nome = Label(frame_login, text='Sistema Login', anchor=NE, font=('Ivy 25'), bg=cor_b, fg=cor_lt)
label_nome.grid(row=0, column=0, padx=1, pady=1)

#--Criando uma label linha dentro do Frame_login--#
label_linha = Label(frame_login, text='', anchor=NW, font=('Ivy 1'), bg=cor_v, width=270)
label_linha.grid(row=1, column=0, padx=1, pady=5)

#--Criando uma Entry dentro do Frame_login--#
entry_nome = Entry(frame_login, text='', font=('Ivy 25'), width=13, justify='left', relief='solid')
entry_nome.grid(row=2, column=0, padx=1, pady=0)

#--Criando uma label Obs dentro do Frame_login--#
label_username = Label(frame_login, text='*O campo de username e obg.', anchor=NE, font=('Ivy 10'), bg=cor_b, fg=cor_lt)
label_username.grid(row=3, column=0, padx=1, pady=5)

#--Criando uma Entry dentro do Frame_login--#
entry_login = Entry(frame_login, text='', font=('Ivy 25'), width=13)
entry_login.grid(row=4, column=0, padx=1, pady=0)

#--Criando uma label Obs dentro do Frame_login--#
label_userlogin = Label(frame_login, text='*O campo de userlogin e obg.', anchor=NE, font=('Ivy 10'), bg=cor_b, fg=cor_lt)
label_userlogin.grid(row=5, column=0, padx=1, pady=0)






janela.mainloop()

