import os
import sqlite3
from sqlite3 import Error

#Funcao que faz a conexao com o banco de dados
def conexaobanco():
    caminho = 'Banco_Login.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return con

vcon = conexaobanco() #variavel que retorna a conexao com o banco de dados

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operacao realizada com sucesso')
        conexao.close()
        os.system('pause')

def menuprincipal():
    os.system('cls')
    print('[1] Cadastrar novo Usuario\n[2] Fazer Login\n[3] Sair')

def menuinserir():
    os.system('cls')
    vnome = input('Digite o seu nome: ')
    vsenha = input('Digite a sua senha: ')
    vsql = "INSERT INTO tb_login(T_NOMECONTATO, T_SENHACONTATO) VALUES ('"+vnome+"', '"+vsenha+"')"
    query(vcon, vsql)

opcao = 0

while opcao != 3:
    menuprincipal()
    try:
        opcao = int(input('Digite a opcao Desejada: '))
        if opcao == 1:
            menuinserir()
            ...
        elif opcao == 2:
            #menuconsutarnome()
            #menuconsultarsenha()
            ...
        elif opcao == 3:
            os.system('cls')
            print('Fim do programa!')
            break
        else:
            os.system('cls')
            print('Opcao Invalida')
            os.system('pause')
    except ValueError:
        os.system('cls')
        print('Opcao Invalida')
os.system('pause')

vcon.close


