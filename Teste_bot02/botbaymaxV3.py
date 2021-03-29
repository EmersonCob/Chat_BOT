import logging
import sqlite3

from sqlite3 import Error
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

###########################################################################################
###########################################################################################
###################################### BOT ################################################
###########################################################################################
###########################################################################################    

########## Entrada do usuario

def entradaInst(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaMed(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaCont(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaContato(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaViz(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaKML(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaImg(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
  

###########################################################################################
###########################################################################################
################################ BOT ######################################################
###########################################################################################
###########################################################################################

########## Verifica se tem mensagem nova

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

########## iniciando o bot

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


###########################################################################################
###########################################################################################
################################## BANCO DE DADOS #########################################
###########################################################################################
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

entradaCont = 4008862601

vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
res=consultaContrato(vcon,vsql)   
if res:
    for r in res:
        for retorno in r:
            print(retorno)
else:
    print(f"\nNúmero invalido ou não localizado!\n")    

vcon.close()

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
        for retorno in r:
            print(retorno)
else:
    print(f"\nNúmero invalido ou não localizado!\n")  

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
        for retorno in r:
            print(retorno)
else:
    print(f"\nNúmero invalido ou não localizado!\n")  

vcon.close()

###########################################################################################################   
###########################################################################################################   
###########################################################################################################   

########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("instalacao", entradaInst))
    dispatcher.add_handler(CommandHandler("medidor", entradaMed))
    dispatcher.add_handler(CommandHandler("contrato", entradaCont))
    dispatcher.add_handler(CommandHandler("contato", entradaContato))
    dispatcher.add_handler(CommandHandler("vizinhos", entradaViz))
    dispatcher.add_handler(CommandHandler("kml", entradaKML))
    dispatcher.add_handler(CommandHandler("imagem", entradaImg))

    # on noncommand i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(consultaInstalacao().retornoInst))
    #dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, medidor))
    #dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, contrato))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()