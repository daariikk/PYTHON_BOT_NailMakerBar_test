from telebot.types import Message
from telebot import types
from loader import bot
from keyboards.inline.inline_markup import start_inline
from keyboards.reply.reply_markup import service_reply
from site_API.utils import site_api_handler
from database.core import insert_command

service_dict = site_api_handler._make_response()

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    insert_command(message.from_user.first_name, command='/start')
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
    bot.reply_to(message, WELCOME_MESSAGE, reply_markup=start_inline())

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    user_id = callback.from_user.id
    if callback.data == 'questions':
        insert_command(callback.from_user.first_name, command='Узнать прайс')
        bot.send_message(user_id, "Выберите услугу:", reply_markup=service_reply())

        bot.register_next_step_handler(callback.message, get_service_name)
    # Ваш код обработки коллбэка

def get_service_name(message: Message):
    print(service_dict[message.text])
    ANSWER_MESSAGE = ''
    for service, cost in service_dict[message.text].items():
        ANSWER_MESSAGE += f'*{service}*  {cost}\n'
    bot.send_message(message.chat.id, ANSWER_MESSAGE, parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())