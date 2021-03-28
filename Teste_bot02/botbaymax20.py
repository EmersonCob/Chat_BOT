import logging


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


