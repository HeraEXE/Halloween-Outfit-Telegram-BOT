from random import choice
from __main__ import bot
from keyboards import get_outfit, no_outfit, start_halloween
from stickers import outfits
from funcs import FUNCS
from phrases import greeting, poem, start_again

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id , greeting, reply_markup=start_halloween)

@bot.message_handler(content_types=['text'])
def get_message(message):
    func = FUNCS.get(message.text)
    if func:
        exec(func)


def halloween(message):
    bot.send_message(message.chat.id, poem, reply_markup=get_outfit)


def receive_outfit(message):
        if outfits:
            fortune = choice(outfits)
            bot.send_message(message.chat.id, 
                f'@{message.from_user.username} получает костюм - {fortune[0]}')
            with open(fortune[1], 'rb') as sticker:
                bot.send_sticker(message.chat.id, sticker)
            try:
                outfits.remove(fortune)
            except ValueError:
                pass  
        else:
            bot.send_message(message.chat.id, 
                                '🥺ВСЕ ОБРАЗЫ РАЗОБРАНЫ', reply_markup=no_outfit)

def cry(message):
    bot.send_message(message.chat.id, start_again)