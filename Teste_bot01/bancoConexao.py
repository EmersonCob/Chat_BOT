import sqlite3
from sqlite3 import Error
from botbaymax import entradaInst, entradaMed, entradaCont

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

######## Consultado por instalação

vsql= f"SELECT * FROM BD_Leitura WHERE instalacao = {entradaInst}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoInst in r: 
        print(retornoInst)


######## Consulta por medidor

vsql= f"SELECT * FROM BD_Leitura WHERE medidor = {entradaMed}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoMed in r: 
        print(retornoMed)

######## Consulta por Conta Contrato

vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoCont in r: 
        print(retornoCont)
