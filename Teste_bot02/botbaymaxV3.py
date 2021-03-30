import logging
import requests
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
    print(contacontrato)
    if len(contacontrato) <= 10:
        message = """Número da conta contrato está incorreto... 
                        \nPor gentileza informe o número correto!"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Segue conforme solicitado: " +  "Ajudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END

def inputContrato2(update, context):
    contacontrato = update.message.text
    message = "Segue conforme solicitado: " + "Ajudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


#def entradaContato(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número da instalação! \n\nEx.: /instalacao 1234567")

#def entradaViz(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número da instalação! \n\nEx.: /instalacao 1234567")

#def entradaKML(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text("Informe o número da MRU! \n\nEx.: /mru 01128101")

#def entradaImg(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text(update.message.text)
  

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
    #dispatcher.add_handler(CommandHandler("contato", entradaContato))
    #dispatcher.add_handler(CommandHandler("vizinhos", entradaViz))
    #dispatcher.add_handler(CommandHandler("kml", entradaKML))
    #dispatcher.add_handler(CommandHandler("imagem", entradaImg))

    #updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('contrato', entradaContrato)],
        states={
            STATE1: [MessageHandler(Filters.text, inputContrato)],
            STATE2: [MessageHandler(Filters.text, inputContrato2)]
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