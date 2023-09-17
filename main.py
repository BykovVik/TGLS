import telebot
from transliterate.base import TranslitLanguagePack, registry
from transliterate import translit
from dotenv import load_dotenv
import os
import re
import enchant

#enchant.set_param("hunspell.dictionary.path", "/usr/share/hunspell/ru_RU.dic")

dictionary = enchant.Dict("en_US")
dictionary_RU = enchant.Dict("ru_RU")
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
    if message.chat.type == "private":
        return
    
    if dictionary.check(message.text.split()[0]):
        return
    
    if dictionary_RU.check(re.sub(r'[.,"\'-?:!;]', '', message.text.split()[0])):
        return
        
    msg = translit(message.text, language_code='kbd')

    if message.text != msg:
        bot.reply_to(message, msg)
    
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        print("Упал")