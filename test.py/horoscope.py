import random
import telebot
from telebot import types

# Замените 'YOUR_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7601514531:AAHtYPDcamHfpAMsiXEEQpma2XgI7orVKmA')

# Списки с возможными сообщениями
first = [
    "Сегодня — идеальный день для новых начинаний.",
    "Постарайтесь не пренебрегать важными решениями.",
    "Будьте готовы к неожиданностям."
]
second = [
    "Но помните, что даже в этом случае нужно не забывать про",
    "Важно сосредоточиться на",
    "Не упустите возможность"
]
second_add = [
    "отношения с друзьями и близкими.",
    "свое здоровье.",
    "долгосрочные планы."
]
third = [
    "Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
    "Обратитесь к своему внутреннему голосу.",
    "Запомните, что удача на вашей стороне."
]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() in ["привет", "/start"]:
        bot.send_message(message.from_user.id, "Привет! Сейчас я расскажу тебе гороскоп на сегодня.")
        
        # Создание клавиатуры
        keyboard = types.InlineKeyboardMarkup()
        zodiac_signs = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']

        for sign in zodiac_signs:
            key = types.InlineKeyboardButton(text=sign, callback_data=sign.lower())
            keyboard.add(key)

        bot.send_message(message.from_user.id, 'Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет' для начала.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши '/help'.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        # Генерация гороскопа
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
    except Exception as e:
        bot.send_message(call.message.chat.id, "Произошла ошибка: {}".format(str(e)))

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)









