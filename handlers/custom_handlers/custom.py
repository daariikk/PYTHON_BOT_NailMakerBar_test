from typing import Dict
from telebot import types
from telebot.types import Message

from keyboards.reply.reply_markup import service_reply
from loader import bot
from handlers.custom_handlers import formatting_service
from database.core import insert_command
@bot.message_handler(commands=["custom"])
def bot_low(message: Message):
    insert_command(message.from_user.first_name, command='/custom')
    bot.reply_to(message, "Выберите услугу:", reply_markup=service_reply())

    bot.register_next_step_handler(message, get_service_name)

def get_service_name(message: Message):

    service_name = message.text
    service_form_list = formatting_service.formatting(service_name)
    bot.reply_to(message, f"Выберите количество категорий: (от 1 до {len(service_form_list[0])})", reply_markup=types.ReplyKeyboardRemove())

    bot.register_next_step_handler(message, get_number, service_form_list)
def get_number(message: Message, format_list_dict: Dict):
    ANSWER_MESSAGE = ''
    try:
        number = int(message.text)
        if 0 < number <= len(format_list_dict[0]):

            bot.reply_to(message, "Введите ценовой диапазон.\nПример ввода '300 - 1500'")
            bot.register_next_step_handler(message, get_range, format_list_dict)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректное число.")

def get_range(message: Message, format_list_dict: Dict):

    # input_data = "111 - 1000"
    if ('-' in message.text and message.text[:message.text.index('-')].strip().isdigit()
        and message.text[message.text.index('-')+1:].strip().isdigit()
        and int(message.text[:message.text.index('-')].strip()) < int(message.text[message.text.index('-')+1:].strip())):
        low = int(message.text[:message.text.index('-')].strip())
        print(low)
        high = int(message.text[message.text.index('-')+1:].strip())
        print(high)
        ANSWER_MESSAGE = ''
        services_name = list()
        for key, item in format_list_dict[0].items():
            if low <= item <= high:
                services_name.append(key)
        for name in services_name:
            ANSWER_MESSAGE += f'*{name}* _ {format_list_dict[2][name]}\n'
        for key in format_list_dict[1].keys():
            ANSWER_MESSAGE += f'*{key}* _ {format_list_dict[1][key]}\n'
        bot.reply_to(message, ANSWER_MESSAGE, parse_mode='Markdown')

    else:
        bot.reply_to(message, "Некорректный формат диапазона. \nПример ввода '300 - 1500'")
        bot.register_next_step_handler(message, get_range, format_list_dict)
