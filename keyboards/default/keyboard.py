from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


key_1 = KeyboardButton('Просмотр фильма 🎬')
key_2 = KeyboardButton('Выйти в город')

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2)
menu.add(key_1, key_2)

key_3 = KeyboardButton('Дома 🏠')
key_4 = KeyboardButton('В кинотеатре 🎥')
key_5 = KeyboardButton('Назад')

place = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2)
place.add(key_3, key_4, key_5)

show = KeyboardButton('Выставки/музеи 🏛️')
circus = KeyboardButton('Цирк 🎪')
performance = KeyboardButton('Вечеринка🎉')
ice_rink = KeyboardButton('Каток ⛸')
otm = KeyboardButton('Назад')

go_city = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2)
go_city.add(show, circus, performance, ice_rink, otm)


