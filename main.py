import telebot
from transliterate.base import TranslitLanguagePack, registry
from transliterate import get_available_language_codes, translit
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

class MyLanguagePack(TranslitLanguagePack):
    language_code = "kbd"
    language_name = "KeyBoard"
    mapping = (
       'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
       'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,йцукенгшщзхъфывапролджэячсмитьбю.',
)

registry.register(MyLanguagePack)


@bot.message_handler(content_types=['text'])
def chat_nessage_hendler(message):
    print("ЭТООО")
    if message.chat.type == "private":
        return
    else:
        
        msg = translit(message.text, language_code='kbd')
        
        if message.text != msg:
            bot.reply_to(message, msg)
    
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        print("Упал")