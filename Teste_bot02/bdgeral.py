import sqlite3

#from botbaymaxV3 import 
from sqlite3 import Error


###########################################################################################
################################## BANCO DE DADOS #########################################
###########################################################################################

########## Criar Conexão com BD e a tabela

########## Realizar Consultas - Por Conta Contrato

def ConexaoBanco():
    caminho = "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db" # caminho do banco - "C:\\Projetos_JEB\\BD_Leitura\\BD_Leitura.db"
    con = None

    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()   

def consultaContrato(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

entradaCont = 2089890015

def resultadoCont():
    vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
    res=consultaContrato(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = {retorno}
                return(resultado)
    else:
        return (f"\nNúmero invalido ou não localizado!\n")
    


saidaFinal = resultadoCont()

vcon.close()

###########################################################################################################   
###########################################################################################################   
########################################################################################################### 