import logging
import requests

import sqlite3

from sqlite3 import Error


from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import Update
from time import sleep
from threading import Thread, Lock


###################################### BOT ################################################

# Versão

def versao(update, context):
    contacontrato = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    print(contacontrato)
    message = f"Olá {firstName} {lastName}!\n\nAtualmente estou na versão 5.0!\n\n Comandos ativos para consulta: \n \n * /contrato; \n * /instalacao; \n * /medidor."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
 
# Consultas

STATE1 = 1
STATE2 = 2

def entradaContrato(update, context):
    try:
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, "+ firstName + " " + lastName + "!" + " \n\nInforme o número da Conta Contrato."
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))

def inputContrato(update, context):
    contacontrato = update.message.text
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    #print(contacontrato)
    if len(contacontrato) < 10:
        message = f"""{firstName} {lastName}!\n\nO número da conta contrato está incorreto. 
                        \nPor gentileza informe o número correto."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        #message = (input("Informe o contrato: "))
        #context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        entrada = contacontrato
        vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entrada}" #interpolação para entrada do usuario
        res=consultaContrato(vcon,vsql)   
        if res:
            for r in [res]:
                for retorno  in r:
                    resultado = retorno
                    #return(resultado)            
        else:
            resultado = "Número invalido ou não localizado!"
            #return (f"Número invalido ou não localizado!")
        messagebd = resultado
        message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        #print(f'teste1{luta}')
        #return entrada, STATE2
        return ConversationHandler.END


def inputContrato2(update, context):
    #contacontrato = update.message.text
    saidaFinal = resultadoCont()
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    messagebd = saidaFinal
    message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

#############################################################3
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
'''
entradaCont = 2089890015 #getNota # falta uma solução para a entrada 

def resultadoCont():
    #entradaCont = inputContrato
    vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
    res=consultaContrato(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = retorno
                return(resultado)            
    else:
        return (f"Número invalido ou não localizado!")
        

#saidaFinal = resultadoCont()
'''

# Verifica se tem mensagem nova

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
 
# Start

def start(update, context):
    username = update.message.from_user.username
    """Send a message when the command /start is issued."""
    update.message.reply_text(f"Olá, {username}!")  

########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAHXc-gyKWwiN4NMrnj340wz84CxpanJ2XY")

    # Get the dispatcher to register handlers
    #dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("instalacao", entradaInst))

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.dispatcher.add_handler(CommandHandler('versao', versao))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('contrato', entradaContrato)],
        states={
            STATE1: [MessageHandler(Filters.text, inputContrato)],   
            STATE2: [MessageHandler(Filters.text, inputContrato2)]
        },
        fallbacks=[CommandHandler('cancelar', cancel)])
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