! / usr / bin / env python
# pylint: disable = C0116
# Este programa é dedicado ao domínio público sob a licença CC0.

"" "
Bot simples para enviar mensagens do Telegram cronometradas.
Este bot usa a classe Updater para lidar com o bot e o JobQueue para enviar
mensagens cronometradas.
Primeiro, algumas funções do manipulador são definidas. Então, essas funções são passadas para
pelo Despachante e registrados em seus respectivos locais.
Em seguida, o bot é iniciado e executado até pressionar Ctrl-C na linha de comando.
Uso:
Exemplo de bot de alarme básico, envia uma mensagem após um tempo definido.
Pressione Ctrl-C na linha de comando ou envie um sinal ao processo para interromper o
robô.
"" "

 registro de importação

da  atualização de importação de telegrama  
do  telegrama . ext  import  Updater , CommandHandler , CallbackContext

# Habilitar registro
registro . basicConfig (
    format = '% (asctime) s -% (name) s -% (levelname) s -% (message) s' , level = logging . INFO
)

logger  =  registro . getLogger ( __name__ )


# Defina alguns manipuladores de comando. Estes geralmente levam os dois argumentos update e
# contexto. Os manipuladores de erro também recebem o objeto TelegramError gerado com erro.
def  start ( update : Update , _ : CallbackContext ) ->  Nenhum :
    atualização . mensagem . reply_text ( 'Olá! Use / set <segundos> para definir um cronômetro' )


def  alarm ( contexto : CallbackContext ) ->  Nenhum :
    "" "Envie a mensagem de alarme." ""
    trabalho  =  contexto . trabalho
    contexto . bot . send_message ( job . context , text = 'Beep!' )


def  remove_job_if_exists ( nome : str , contexto : CallbackContext ) ->  bool :
    "" "Remover trabalho com o nome fornecido. Retorna se o trabalho foi removido." ""
    current_jobs  =  contexto . job_queue . get_jobs_by_name ( nome )
    se  não  current_jobs :
        retornar  falso
    para  trabalho  em  current_jobs :
        trabalho . schedule_removal ()
    retornar  verdadeiro


def  set_timer ( update : Update , context : CallbackContext ) ->  None :
    "" "Adicionar um trabalho à fila." ""
    chat_id  =  atualização . mensagem . chat_id
    tente :
        # args [0] deve conter o tempo do cronômetro em segundos
        devido  =  int ( contexto . args [ 0 ])
        se  devido  <  0 :
            atualização . mensagem . reply_text ( 'Desculpe, não podemos voltar ao futuro!' )
            Retorna

        job_removed  =  remove_job_if_exists ( str ( chat_id ), contexto )
        contexto . job_queue . run_once ( alarme , devido , contexto = chat_id , nome = str ( chat_id ))

        text  =  'Timer definido com sucesso!'
        se  job_removed :
            text  + =  'O antigo foi removido.'
        atualização . mensagem . reply_text ( texto )

    exceto ( IndexError , ValueError ):
        atualização . mensagem . reply_text ( 'Uso: / set <segundos>' )


def  não definido ( atualizar : Atualizar , contexto : CallbackContext ) ->  Nenhum :
    "" "Remova o trabalho se o usuário mudar de ideia." ""
    chat_id  =  atualização . mensagem . chat_id
    job_removed  =  remove_job_if_exists ( str ( chat_id ), contexto )
    text  =  'Timer cancelado com sucesso!'  if  job_removed  else  'Você não tem um cronômetro ativo.'
    atualização . mensagem . reply_text ( texto )


def  main () ->  Nenhum :
    "" "Executar bot." ""
    # Crie o Updater e passe a ele o token do seu bot.
    atualizador  =  Updater ( "token" )

    # Faça com que o despachante registre manipuladores
    despachante  =  atualizador . expedidor

    # em comandos diferentes - responder no telegrama
    despachante . add_handler ( CommandHandler ( "start" , start ))
    despachante . add_handler ( CommandHandler ( "ajuda" , início ))
    despachante . add_handler ( CommandHandler ( "set" , set_timer ))
    despachante . add_handler ( CommandHandler ( "unset" , unset ))

    # Inicie o bot
    atualizador . start_polling ()

    # Bloquear até que você pressione Ctrl-C ou o processo recebe SIGINT, SIGTERM ou
    # SIGABRT. Isso deve ser usado na maioria das vezes, uma vez que start_polling () é
    # sem bloqueio e irá parar o bot normalmente.
    atualizador . inativo ()


if  __name__  ==  '__main__' :
    principal ()