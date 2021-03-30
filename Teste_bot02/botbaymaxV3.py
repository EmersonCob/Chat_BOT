import logging
import requests

import sqlite3

from sqlite3 import Error

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import Update


###########################################################################################
###################################### BOT ################################################
###########################################################################################

########## Entrada do usuario

#def entradaInst(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número da instalação! \n\nEx.: /instalacao 1234567")

#def entradaMed(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número do equipamento de medição! \n\nEx.: /medidor 7012345678")

STATE1 = 1
STATE2 = 2


def entradaContrato(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, "+ firstName + " " + lastName + "!" + " \n\nInforme o número da conta contrato."
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))


def inputContrato(update, context):
    contacontrato = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    print(contacontrato)
    if len(contacontrato) < 10:
        message = f"""{firstName} {lastName}!\n\nNúmero da conta contrato está incorreto. 
                        \nPor gentileza informe o número correto."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        #numberCont = str(context.args)
        messagebd = saidaFinal
        message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputContrato2(update, context):
    contacontrato = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    #numberCont = str(context.args)
    messagebd = saidaFinal
    message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


STATE3 = 3
STATE4 = 4


def entradaInstalacao(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, "+ firstName + " " + lastName + "!" + " \n\nInforme o número da instalação."
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE3
    except Exception as e:
        print(str(e))


def inputInstalacao(update, context):
    instalacao = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    print(instalacao)
    if len(instalacao) < 6:
        message = f"""{firstName} {lastName}!\n\nNúmero da instalação está incorreta. 
                        \nPor gentileza informe o número correto."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE3
    else:
        #numberCont = str(context.args)
        messagebd = saidaFinal
        message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputInstalacao2(update, context):
    instalacao = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    #numberCont = str(context.args)
    messagebd = saidaFinal
    message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


STATE5 = 5
STATE6 = 6


def entradaMedidor(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, "+ firstName + " " + lastName + "!" + " \n\nInforme o número do Medidor."
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE5
    except Exception as e:
        print(str(e))


def inputMedidor(update, context):
    medidor = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    print(medidor)
    if len(medidor) < 5:                                                
        message = f"""{firstName} {lastName}!\n\nO número do medidor está incorreto. 
                        \nPor gentileza informe o número correto."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE5
    else:
        #numberCont = str(context.args)
        messagebd = saidaFinal
        message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputMedidor2(update, context):
    medidor = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    #numberCont = str(context.args)
    messagebd = saidaFinal
    message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


#def entradaContato(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número da instalação! \n\nEx.: /instalacao 1234567")

###########################################################################################
################################## BANCO DE DADOS #########################################
###########################################################################################

########## Criar Conexão com BD e a tabela

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
                resultado = retorno
                return(resultado)
    else:
        return (f"Número invalido ou não localizado!")
    


saidaFinal = resultadoCont()

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

entradaInst = 475452

def resultadoInst():
    vsql= f"SELECT * FROM BD_Leitura WHERE instalacao = {entradaInst}" #interpolação para entrada do usuario
    res=consultaInstalacao(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = retorno
                return(resultado)
    else:
        return (f"Número invalido ou não localizado!")
    

saidaFinal = resultadoInst()

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

entradaMed = "W78170"

def resultadoMed():
    vsql= f"SELECT * FROM BD_Leitura WHERE medidor LIKE '%{entradaMed}%'" #interpolação para entrada do usuario
    res=consultaMedidor(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = retorno
                return(resultado)
    else:
        return (f"Número invalido ou não localizado!")
    

saidaFinal = resultadoMed()

vcon.close()


###########################################################################################
################################ BOT ######################################################
###########################################################################################

########## Verifica se tem mensagem nova

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

########## iniciando o bot

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')  

########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94")

    # Get the dispatcher to register handlers
    #dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("instalacao", entradaInst))
    #dispatcher.add_handler(CommandHandler("medidor", entradaMed))
    #dispatcher.add_handler(CommandHandler("contrato", entradaContrato))

    #updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('contrato', entradaContrato)],
        states={
            STATE1: [MessageHandler(Filters.text, inputContrato)],
            STATE2: [MessageHandler(Filters.text, inputContrato2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)    

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('medidor', entradaMedidor)],
        states={
            STATE5: [MessageHandler(Filters.text, inputMedidor)],
            STATE6: [MessageHandler(Filters.text, inputMedidor2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)  

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('instalacao', entradaInstalacao)],
        states={
            STATE3: [MessageHandler(Filters.text, inputInstalacao)],
            STATE4: [MessageHandler(Filters.text, inputInstalacao2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)  

    # on noncommand i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(consultaInstalacao().retornoInst))
    #dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, medidor))
    #dispatcher.add_handler(MessageHandler(Filters.command, resultadoCont))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()