
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from bancoConexao import retornoInst, retornoMed, retornoCont #resultado da consulta ao BD através da chamada do usuario

########## Verifica se tem mensagem nova

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

########## iniciando o bot

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

########## Entrada do usuario

def entradaInst(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaMed(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def entradaCont(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
  
########## BOT 

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1757548140:AAGqdAGKSoIDJLCIB_NxuQM1TSpKO1RkG94")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("instalacao", entradaInst))
    dispatcher.add_handler(CommandHandler("medidor", entradaMed))
    dispatcher.add_handler(CommandHandler("contrato", entradaCont))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, instalacao))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, medidor))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, contrato))

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

# entradaInst, entradaMed, entradaCont