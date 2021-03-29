import sqlite3

from sqlite3 import Error

###########################################################################################
###########################################################################################
################################## BANCO DE DADOS #########################################
###########################################################################################
###########################################################################################

########## Criar Conexão com BD e a tabela
def ConexaoBanco():
    caminho = "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db" # caminho do banco - "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db"
    con = None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()   

########## Realizar Consultas - Por Conta Contrato
def consultaContrato(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

entradaCont = 40088626001

def resultadoCont():
    vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
    res=consultaContrato(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = {retorno}
                print(resultado)
    else:
        print(f"\nNúmero invalido ou não localizado!\n")          

resultadoCont()

vcon.close()

'''
instalacao = ('Instalação: ')
                medidor = ('Medidor: ')
                contrato = ('Contrato: ')
                area = ('Area: ')
                rota = ('Rota: ')
                lote = ('Lote: ')
                mru = ('MRU: ')
                link = ('Localização: ')
                sequencia = ('Sequencia: ')
                nome = ('Cliente: ')
                endereco = ('Endereço: ')
                numero = ('Número: ')
                poste = ('Poste: ')
                cidade = ('Cidade: ')
                nota = ('Nota: ')
                comentario = ('Comentario: ')
                leiturista = ('Leiturista: ')

'''




########## Realizar Consultas - Por Medidor

def ConexaoBanco():
    caminho = "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db" # caminho do banco - "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db"
    con = None

    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco() 

def consultaMedidor(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

entradaMed = 3009018774

vsql= f"SELECT * FROM BD_Leitura WHERE medidor LIKE '%{entradaMed}%' " #interpolação para entrada do usuario
res=consultaMedidor(vcon,vsql) 
if res:
    for r in res:
         for retorno  in r:
            resultado = {retorno}
else:
    f"\nNúmero invalido ou não localizado!\n" 

vcon.close()

########## Realizar Consultas - Por Instalação

def ConexaoBanco():
    caminho = "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db" # caminho do banco - "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db"
    con = None

    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco() 

def consultaInstalacao(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

entradaInst = 475481

vsql= f"SELECT * FROM BD_Leitura WHERE instalacao = {entradaInst}" #interpolação para entrada do usuario
res=consultaInstalacao(vcon,vsql) 
if res:
    for r in res:
         for retorno  in r:
            resultado = {retorno}
else:
    f"\nNúmero invalido ou não localizado!\n" 

vcon.close()
