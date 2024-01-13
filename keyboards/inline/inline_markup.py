from telebot import types

def start_inline():
    markup_start = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Узнать прайс', callback_data='questions')
    markup_start.add(button)

    return markup_start

