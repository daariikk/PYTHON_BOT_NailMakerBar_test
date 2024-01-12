from typing import Dict
import time
from telebot.types import Message
from telebot import types


from loader import bot
from handlers.custom_handlers import formatting_service
from keyboards.reply.reply_markup import service_reply
from database.core import insert_command
@bot.message_handler(commands=["low"])
def bot_low(message: Message):
    insert_command(message.from_user.first_name, command='/low')
    bot.reply_to(message, "Выберите услугу:", reply_markup=service_reply())
    time.sleep(1)
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
            first_services_name = list(format_list_dict[0].keys())[:number]
            for name in first_services_name:
                ANSWER_MESSAGE += f'*{name}*  {format_list_dict[2][name]}\n'
            for key in format_list_dict[1].keys():
                ANSWER_MESSAGE += f'*{key}*  {format_list_dict[1][key]}\n'
        bot.reply_to(message, ANSWER_MESSAGE, parse_mode='Markdown')
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректное число.")


#