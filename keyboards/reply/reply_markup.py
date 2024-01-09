from telebot import types

def service_reply():
    markup_service = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Маникюр')
    btn2 = types.KeyboardButton(text='Педикюр')
    btn3 = types.KeyboardButton('Покрытие')
    btn4 = types.KeyboardButton('Дизайны')
    btn5 = types.KeyboardButton('Наращивание ногтей')
    btn6 = types.KeyboardButton('Дополнительные услуги')
    btn7 = types.KeyboardButton('Brow Bar')
    btn8 = types.KeyboardButton('Ламинирование бровей')
    btn9 = types.KeyboardButton('Макияж')
    btn10 = types.KeyboardButton('Наращивание ресниц')
    btn11 = types.KeyboardButton('Ламинирование ресниц')
    btn12 = types.KeyboardButton('Прически')
    markup_service.row(btn1, btn2, btn12)
    markup_service.row(btn3, btn4,btn7)
    markup_service.row(btn9, btn6)
    markup_service.row(btn5)
    markup_service.row(btn8)
    markup_service.row(btn11)
    markup_service.row(btn10)

    return markup_service

