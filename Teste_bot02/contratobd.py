import sqlite3

#from botbaymax20 import entradaCont1
from sqlite3 import Error

###########################################################################################
###########################################################################################
####################### BANCO DE DADOS - Contrato #########################################
###########################################################################################
###########################################################################################

########## Criar Conexão com BD e a tabela
def conexaoBanco():
    caminho = "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db" # caminho do banco - "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db"
    con = None

    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=conexaoBanco()   

########## Realizar Consultas
def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

######## Consulta por Conta Contrato
entradaCont = 7027778881

vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoCont in r: 
        print(retornoCont)