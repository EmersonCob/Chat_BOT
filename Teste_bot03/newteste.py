import telepot, wikipedia
from telepot.loop import MessageLoop

bot = telepot.Bot("1757548140:AAHXc-gyKWwiN4NMrnj340wz84CxpanJ2XY")
wikipedia.set_lang("pt")

def handle(msg):
    if "text" in msg:
        if msg["text"].startswith("/oquee"):
            lista_palavras = wikipedia.search(msg["text"].replace("/oquee"," "))
            if lista_palavras:
                resumo = wikipedia.page(lista_palavras[0]).summary
                bot.sendMessage(msg["from"]["id"],resumo)
            else:
                bot.sendMessage(msg["from"]["id"],"Nada foi encontrado. ")
        else:
            bot.sendMessage(msg["from"]["id"],"Comando Inválido. ")
    else:
        bot.sendMessage(msg["from"]["id"],"Comando Inválido. ")

MessageLoop(bot, handle).run_as_thread()  

while True:
    pass
