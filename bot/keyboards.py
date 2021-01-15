from telebot.types import ReplyKeyboardMarkup, KeyboardButton

start_halloween = ReplyKeyboardMarkup(resize_keyboard=True)
start_halloween_button = KeyboardButton('🌕HALLOWEEN🌕')
start_halloween.add(start_halloween_button)

get_outfit = ReplyKeyboardMarkup(resize_keyboard=True)
halloween_outfit = KeyboardButton('🕷HALLOWEEN OUTFIT')
get_outfit.add(halloween_outfit)

no_outfit = ReplyKeyboardMarkup(resize_keyboard=True)
tears = KeyboardButton('😭😭😭😭😭😭😭')
no_outfit.add(tears)