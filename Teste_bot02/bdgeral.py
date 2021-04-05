import sqlite3

from sqlite3 import Error


#from botbaymaxV3 import inputContrato


# BANCO DE DADOS 

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

# Realizar Consultas - Por Conta Contrato

entradaCont = 2089890015 #getNota # falta uma solução para a entrada 

def resultadoCont():
    vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
    res=consultaContrato(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = retorno
                return(resultado)            
    else:
        return (f"Número invalido ou não localizado!")
        

saidaFinal = resultadoCont()

ConexaoBanco.close()
