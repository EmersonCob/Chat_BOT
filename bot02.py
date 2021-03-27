from telegram.ext import Updater, CommandHandler
from config import token

def olaMundo(bot, update):
    id_chat = update.message.chat_id
    print(id_chat)
    bot.send_message(chat_id=id_chat, text="Olá mundo")

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ola',olaMundo))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()