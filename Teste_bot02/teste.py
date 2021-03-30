import sqlite3

from sqlite3 import Error


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
                resultado = {retorno}
                print(resultado)
    else:
        prints (f"\nNúmero invalido ou não localizado!\n")
    

def saidaDados():
    print(resultadoCont())

saidaDados()



###########################################################################################
###########################################################################################
################################## BANCO DE DADOS #########################################
###########################################################################################
###########################################################################################

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

########## Realizar Consultas - Por Conta Contrato
def consultaContrato(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

entradaCont = 40088626001

def resultadoCont():
    vsql= f"SELECT * FROM BD_Leitura WHERE contrato = {entradaCont}" #interpolação para entrada do usuario
    res=consultaContrato(vcon,vsql)   
    if res:
        for r in [res]:
            for retorno  in r:
                resultado = {retorno}
                print(resultado)
    else:
        print(f"\nNúmero invalido ou não localizado!\n")          

resultadoCont()

vcon.close()


instalacao = ('Instalação: ')
                medidor = ('Medidor: ')
                contrato = ('Contrato: ')
                area = ('Area: ')
                rota = ('Rota: ')
                lote = ('Lote: ')
                mru = ('MRU: ')
                link = ('Localização: ')
                sequencia = ('Sequencia: ')
                nome = ('Cliente: ')
                endereco = ('Endereço: ')
                numero = ('Número: ')
                poste = ('Poste: ')
                cidade = ('Cidade: ')
                nota = ('Nota: ')
                comentario = ('Comentario: ')
                leiturista = ('Leiturista: ')





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
         for retorno  in r:
            resultado = {retorno}
else:
    f"\nNúmero invalido ou não localizado!\n" 

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
         for retorno  in r:
            resultado = {retorno}
else:
    f"\nNúmero invalido ou não localizado!\n" 

vcon.close()


##################################################################################################


import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Olá, " + firstName + " " + lastName + ", Let's Start!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def feedback(update, context):
    try:
        message = 'Por favor, digite um feedback para ajudar com o nosso crescimento:'
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))


def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) > 10:
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigado pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigado pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END


# https://getemoji.com/
def askForNota(update, context):
    try:
        question = 'Qual nota você dá para o tutorial?'
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("👎 1", callback_data='1'),
              InlineKeyboardButton("2", callback_data='2'),
              InlineKeyboardButton("🤔 3", callback_data='3'),
              InlineKeyboardButton("4", callback_data='4'),
              InlineKeyboardButton("👍 5", callback_data='5')]])
        update.message.reply_text(question, reply_markup=keyboard)
    except Exception as e:
        print(str(e))


def getNota(update, context):
    try:
        query = update.callback_query
        print(str(query.data))
        message = 'Obrigado pela sua nota: ' + str(query.data) 
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def cancel(update, context):
    return ConversationHandler.END

# aqui

STATE3 = 3
STATE4 = 4

def instalacao(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Por favor, "+ firstName + " " + lastName + " entre com o número da instalação!"
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE3
    except Exception as e:
        print(str(e))


def inputInstalacao(update, context):
    instalacao = update.message.text
    print(instalacao)
    if len(instalacao) < 7:
        message = """Número da instalação está incorreta... 
                        \nPor gentileza informe o número correto!"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE3
    else:
        message = "Segue conforme solicitado: " +  "Ajudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END

def inputInstalacao2(update, context):
    instalacao = update.message.text
    message = "Segue conforme solicitado: " + "Ajudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END


STATE5 = 5
STATE6 = 6


def contacontrato(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Por favor, "+ firstName + " " + lastName + " entre com o número da conta contrato!"
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE5
    except Exception as e:
        print(str(e))


def inputContacontrato(update, context):
    contacontrato = update.message.text
    print(contacontrato)
    if len(contacontrato) < 10:
        message = """Número da conta contrato está incorreto... 
                        \nPor gentileza informe o número correto!"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE5
    else:
        message = "Segue conforme solicitado: " +  "Ajudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END

def inputContacontrato2(update, context):
    contacontrato = update.message.text
    message = "Segue conforme solicitado: " + "Ajudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

STATE7 = 7
STATE8 = 8


def medicao(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = "Por favor, "+ firstName + " " + lastName + " entre com o número do equipamento de medição!"
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE7
    except Exception as e:
        print(str(e))


def inputMedicao(update, context):
    medicao = update.message.text
    print(medicao)
    if len(medicao) < 8:
        message = """O número da medição está incorreto... 
                        \nPor gentileza informe o número correto!"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE7
    else:
        message = "Segue conforme solicitado: " +  "Ajudo em algo mais?"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END

def inputMedicao2(update, context):
    medicao = update.message.text
    message = "Segue conforme solicitado: " + "Ajudo em algo mais?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

# aqui



def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        token = '1566848654:AAEBS9TcwAHm5wh93Z5BtQoi9k5UB44doYg'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', welcome))

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('feedback', feedback)],
            states={
                STATE1: [MessageHandler(Filters.text, inputFeedback)],
                STATE2: [MessageHandler(Filters.text, inputFeedback2)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        # aqui

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('instalacao', instalacao)],
            states={
                STATE3: [MessageHandler(Filters.text, inputInstalacao)],
                STATE4: [MessageHandler(Filters.text, inputInstalacao2)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('contacontrato', contacontrato)],
            states={
                STATE5: [MessageHandler(Filters.text, inputContacontrato)],
                STATE6: [MessageHandler(Filters.text, inputContacontrato2)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('medicao', medicao)],
            states={
                STATE7: [MessageHandler(Filters.text, inputMedicao)],
                STATE8: [MessageHandler(Filters.text, inputMedicao2)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        # aqui

        updater.dispatcher.add_handler(CommandHandler('nota', askForNota))
        updater.dispatcher.add_handler(CallbackQueryHandler(getNota))

        print("Updater no ar: " + str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()

'''