from tg_API.bot import bot
from telebot.types import Message

@bot.message_handler(commands=['start'])
def main(message: Message):
    WELCOME_MESSAGE = """
    Привет! 👋 Добро пожаловать в NailMakerBar — твое уютное место для заботы о себе и поддержания стильного образа! 🌸💅

Мы готовы предложить тебе лучшие услуги, созданные с любовью и вниманием к деталям. В нашем ассортименте разнообразные процедуры для ухода за ногтями, которые подчеркнут твою индивидуальность.

🌟 Наши услуги:
•	Маникюр
•	Педикюр
•	Покрытие
•	Дизайны
•	Наращивание ногтей
•	Доп услуги
•	Brow Bar
•	Ламинирование бровей
•	Макияж
•	Наращивание ресниц
•	Ламинирование ресниц 
•	Причёски

💄 Мы работаем с профессиональными мастерами, используем качественные материалы и следим за последними трендами в мире нейл-индустрии. Твоя красота — наш приоритет!
📌 Заинтересован(а) узнать подробнее о наших услугах и ценах? Просто спроси, и мы с удовольствием поделимся всей необходимой информацией.
"""
    bot.send_message(message.chat.id, WELCOME_MESSAGE)

@bot.message_handler(commands=['help'])
def func_help(message):
    pass

@bot.message_handler(commands=['low'])
def func_low(message):
    pass

@bot.message_handler(commands=['high'])
def func_high(message):
    pass

@bot.message_handler(commands=['custom'])
def func_custom(message):
    pass

@bot.message_handler(commands=['history'])
def history(message):
    pass

@bot.message_handler()
def default():
    pass
