#! / usr / bin / env python
# pylint: disable = C0116
# Este programa é dedicado ao domínio público sob a licença CC0.

"" "Bot que explica a funcionalidade" Deep Linking Parameters "do Telegram.
Este programa é dedicado ao domínio público sob a licença CC0.
Este bot usa a classe Updater para lidar com o bot.
Primeiro, algumas funções do manipulador são definidas. Então, essas funções são passadas para
pelo Despachante e registrados em seus respectivos locais.
Em seguida, o bot é iniciado e executado até pressionar Ctrl-C na linha de comando.
Uso:
Exemplo de Deep Linking. Envie / comece para obter o link.
Pressione Ctrl-C na linha de comando ou envie um sinal ao processo para interromper o
robô.
"" "

 registro de importação

from  telegram  import  ParseMode , InlineKeyboardMarkup , InlineKeyboardButton , Update
do  telegrama . importação ext  (
    Updater ,
    CommandHandler ,
    CallbackQueryHandler ,
    Filtros ,
    CallbackContext ,
)

# Habilitar registro
do  telegrama . utils  import  helpers

registro . basicConfig (
    format = "% (asctime) s -% (name) s -% (levelname) s -% (message) s" , level = logging . INFO
)

logger  =  registro . getLogger ( __name__ )

# Defina constantes que nos permitirão reutilizar os parâmetros de links diretos.
CHECK_THIS_OUT  =  "verificar isso"
USING_ENTITIES  =  "usando-entidades aqui"
USING_KEYBOARD  =  "using-keyboard-here"
SO_COOL  =  "tão legal"

# Dados de retorno de chamada para passar em links diretos de terceiro nível
KEYBOARD_CALLBACKDATA  =  "teclado-callback-data"


def  start ( update : Update , context : CallbackContext ) ->  None :
    "" "Enviar um URL com link direto quando o comando / start for emitido." ""
    bot  =  contexto . robô
    url  =  ajudantes . create_deep_linked_url ( bot . nome de usuário , CHECK_THIS_OUT , grupo = True )
    text  =  "Sinta-se à vontade para contar a seus amigos sobre isso: \ n \ n "  +  url
    atualização . mensagem . reply_text ( texto )


def  deep_linked_level_1 ( update : Update , context : CallbackContext ) ->  Nenhum :
    "" "Alcançado por meio da carga útil CHECK_THIS_OUT" ""
    bot  =  contexto . robô
    url  =  ajudantes . create_deep_linked_url ( bot . nome de usuário , SO_COOL )
    text  = (
        "Incrível, você acabou de acessar a funcionalidade oculta!"
        "Agora vamos voltar ao bate-papo privado."
    )
    teclado  =  InlineKeyboardMarkup . from_button (
        InlineKeyboardButton ( text = "Continue aqui!" , Url = url )
    )
    atualização . mensagem . reply_text ( texto , reply_markup = teclado )


def  deep_linked_level_2 ( update : Update , context : CallbackContext ) ->  Nenhum :
    "" "Alcançado através da carga útil SO_COOL" ""
    bot  =  contexto . robô
    url  =  ajudantes . create_deep_linked_url ( bot . nome de usuário , USING_ENTITIES )
    text  =  f "Você também pode mascarar os URLs com links diretos como links: [▶ ️ CLIQUE AQUI] ( { url } )."
    atualização . mensagem . reply_text ( text , parse_mode = ParseMode . MARKDOWN , disable_web_page_preview = True )


def  deep_linked_level_3 ( update : Update , _ : CallbackContext ) ->  Nenhum :
    "" "Atingido por meio da carga útil de USING_ENTITIES" ""
    atualização . mensagem . reply_text (
        "Também é possível fazer links diretos usando InlineKeyboardButtons." ,
        reply_markup = InlineKeyboardMarkup (
            [[ InlineKeyboardButton ( text = "Assim!" , Callback_data = KEYBOARD_CALLBACKDATA )]]
        ),
    )


def  deep_link_level_3_callback ( atualização : atualização , contexto : CallbackContext ) ->  Nenhum :
    "" "Responde a CallbackQuery com url de link direto." ""
    bot  =  contexto . robô
    url  =  ajudantes . create_deep_linked_url ( bot . nome de usuário , USING_KEYBOARD )
    atualização . callback_query . resposta ( url = url )


def  deep_linked_level_4 ( update : Update , context : CallbackContext ) ->  Nenhum :
    "" "Alcançado através da carga útil USING_KEYBOARD" ""
    carga útil  =  contexto . args
    atualização . mensagem . reply_text (
        f "Parabéns! Isso é o mais profundo possível 👏🏻 \ n \ n A carga útil era: { carga útil } "
    )


def  main () ->  Nenhum :
    "" "Inicie o bot." ""
    # Crie o Updater e passe a ele o token do seu bot.
    atualizador  =  Updater ( "token" )

    # Faça com que o despachante registre manipuladores
    despachante  =  atualizador . expedidor

    # Mais informações sobre o que é realmente um deep linking (leia isto primeiro se não estiver claro para você):
    # https://core.telegram.org/bots#deep-linking

    # Registre um gerenciador de links diretos
    despachante . add_handler (
        CommandHandler ( "start" , deep_linked_level_1 , Filters . Regex ( CHECK_THIS_OUT ))
    )

    # Este funciona com um link textual em vez de um URL
    despachante . add_handler ( CommandHandler ( "start" , deep_linked_level_2 , Filters . regex ( SO_COOL )))

    # Também podemos passar a carga útil do link direto
    despachante . add_handler (
        CommandHandler ( "start" , deep_linked_level_3 , Filters . Regex ( USING_ENTITIES ), pass_args = True )
    )

    # Possível também com botões do teclado embutido
    despachante . add_handler (
        CommandHandler ( "start" , deep_linked_level_4 , Filters . Regex ( USING_KEYBOARD ))
    )

    # registrar o manipulador de retorno de chamada para o botão do teclado embutido
    despachante . add_handler (
        CallbackQueryHandler ( deep_link_level_3_callback , pattern = KEYBOARD_CALLBACKDATA )
    )

    # Certifique-se de que os manipuladores de links diretos ocorram * antes * do manipulador normal / start.
    despachante . add_handler ( CommandHandler ( "start" , start ))

    # Inicie o bot
    atualizador . start_polling ()

    # Execute o bot até pressionar Ctrl-C ou o processo recebe SIGINT,
    # SIGTERM ou SIGABRT. Isso deve ser usado na maioria das vezes, uma vez que
    # start_polling () não bloqueia e irá parar o bot normalmente.
    atualizador . inativo ()


if  __name__  ==  "__main__" :