from config import URL_TELEGRAM_BASE
import requests


resposta = requests.post(URL_TELEGRAM_BASE + "/getUpdates")

resposta = resposta.json()

for item in resposta['result']:

    if 'photo' in item['message']:

        print('Foto encontrada')

    else:
        conteudo = {
            'chat_id': item['message']['chat']['id'],
            'text': 'Por favor, enviar somente imagens.',
            'reply_to_message_id': item['message']['message_id']
        }

        requests.post(URL_TELEGRAM_BASE + "/sendMessage", data=conteudo)

        print('Texto encontrado')