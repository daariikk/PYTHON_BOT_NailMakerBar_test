
from telebot.types import Message
from loader import bot
from database.core import check_database, insert_command

@bot.message_handler(commands=["history"])
def bot_history(message: Message):
    insert_command(message.from_user.first_name, command='/history')
    bot.reply_to(message, check_database())

