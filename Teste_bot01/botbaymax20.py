import logging
import sqlite3

from sqlite3 import Error
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

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
  
########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("instalacao", retornoInst))
    dispatcher.add_handler(CommandHandler("medidor", entradaMed))
    dispatcher.add_handler(CommandHandler("contrato", entradaCont))
    dispatcher.add_handler(CommandHandler("contato", entradaContato))
    dispatcher.add_handler(CommandHandler("vizinhos", entradaViz))
    dispatcher.add_handler(CommandHandler("kml", entradaKML))
    dispatcher.add_handler(CommandHandler("imagem", entradaImg))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, [retornoInst]))
    #dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, medidor))
    #dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, contrato))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()


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

vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoCont in r: 
    print(retornoCont)

###########################################################################################
###########################################################################################
######################### BANCO DE DADOS - Medidor ########################################
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

######## Consulta por medidor

vsql= f"SELECT * FROM BD_Leitura WHERE medidor LIKE '%{entradaMed}%' " #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoMed in r: 
        print(retornoMed)

###########################################################################################
###########################################################################################
######################### BANCO DE DADOS - Instalação #####################################
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

######## Consultado por instalação

vsql= f"SELECT * FROM BD_Leitura WHERE instalacao = {entradaInst}" #interpolação para entrada so usuario
res=consulta(vcon,vsql) 

for r in res:
    for retornoInst in r: 
        print(retornoInst)
