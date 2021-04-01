import logging
import requests
import time
import json
import sqlite3

from sqlite3 import Error

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import Update
from time import sleep
from threading import Thread, Lock


###################################### BOT ################################################

class TelegramBot:
    def __init__(self):
        token = '1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94'
        url_base = f'https://api.telegram.org/bot{token}'
    
    # Iniciar o bot
    def Iniciar(self):
        Update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    resposta = self.criar_resposta()
                    self.responder(resposta,chat_id)
    # Obter mensagens
    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json(resultado.content)    
    # Criar uma resposta
    def criar_resposta(self):
        return 'Olá, bem vindo ao nosso bot!'

    # Responder 
    def responder(self, resposta, chat_id):
        #enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()




























'''

STATE1 = 1
STATE2 = 2

def entradaContrato(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, "+ firstName + " " + lastName + "!" + " \n\nInforme o número da Conta Contrato."
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
        message = f"""{firstName} {lastName}!\n\nO número da conta contrato está incorreto. 
                        \nPor gentileza informe o número correto."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    else:
        messagebd = saidaFinal
        message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputContrato2(update, context):
    contacontrato = update.message.text
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    messagebd = saidaFinal
    message = f"{firstName} {lastName}, segue conforme solicitado:\n\n {messagebd} \n\nAjudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


################################## BANCO DE DADOS #########################################

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

def consultaContrato(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

########## Realizar Consultas - Por Conta Contrato

entradaCont = 2089890015 # falta uma solução para a entrada 

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

################################ BOT ######################################################

########## Verifica se tem mensagem nova

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

########## iniciando o bot

def start(update, context):
    username = update.message.from_user.username
    """Send a message when the command /start is issued."""
    update.message.reply_text(f"Olá, {username}!")  

########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94")

    # Get the dispatcher to register handlers
    #dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("instalacao", entradaInst))

    updater.dispatcher.add_handler(CommandHandler('start', start))

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

    '''