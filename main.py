import telebot

import random

from telebot import types

bot = telebot.TeleBot('6183689675:AAGge8NECMU_ogVsJvGcsTB5ImyTDkW_91c')

first = ["Каким бы трудным ни был этот день...","Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, не игнорируйте тревоги.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Цитата дня – «Как говорил мой дед - я твой дед».","Плодотворный день для того, чтобы разобраться с накопившимися делами.","На самом деле, неплохой апрельский денёк.","Очередной день полномасштабного вторжения. Но мы ведь уже привыкли.","Ну что ж.","Хуй завёрнутый в газету – заменяет сигарету.","Весна 2023.","Даже не знаю, сказать... Скажу, как есть.","Слава Украине!"]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны не забывать про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про","Всегда приятно думать про","Возможно, сегодня стоило бы просто расслабиться и подумать про","А ведь здорово было бы нассать на","А знаешь, что тебя сегодня может порадовать? Просто попробуй посмотреть на","А ЗСУ ебашат шо хуярят и просто ссут на"]
second_add = ["такие милые разорванные ебальники орков.","разъёбанные танки свинособак.","копчёную орочью технику.","разорванную в мясо орковскую броню.","дохлых руснявых пидоров.","то, как рфские выблядки ссутся контрнаступления.","свинособачек, падающих сотнями каждый день.","сосущих хуй додиков, которые пришли брать Киев за 3 дня.","(не)успехи МинОтсоса расеи.","глотающих хуй расеян.","немощные попытки русни сделать хоть что-то."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Венера сегодня в Марсе, а у русни во рту хуй.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты.","Мы однозначно победим.","В нашей победе уж точно не стоит сомневаться.","А у тебя - всё будет хорошо.","Все буде добре.","В принципе, звёзды сегодня на твоей стороне, ты ж не русня.","Я, конечно, не чек из Сильпо, но всё же, предсказываю тебе удачу в скорем времени.","Все буде Україна.","Так шо не грусти.","В целом, звёзды говорят, шо всё будет чётко."]


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    mess = 'Напиши "ебани гороскоп", и я ебану'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Слава Украине":
        bot.send_message(message.chat.id, "Героям слава", parse_mode='html')
    elif "лава Укра" in message.text:
        bot.send_message(message.chat.id, "Героям слава!", parse_mode='html')
    elif "лава нац" in message.text:
        bot.send_message(message.chat.id, "Смерть ворогам!", parse_mode='html')
    elif message.text == "Слава Україні!":
        bot.send_message(message.chat.id, "<b>Героям слава!</b>", parse_mode='html')
    elif message.text == "русня":
        bot.send_message(message.chat.id, "пидарасы", parse_mode='html')
    elif "путин" in message.text:
        bot.send_message(message.chat.id, "хуйло", parse_mode='html')
    elif "путін" in message.text:
        bot.send_message(message.chat.id, "хуйло", parse_mode='html')
    elif "Путін" in message.text:
        bot.send_message(message.chat.id, "хуйло", parse_mode='html')
    elif "ивси" in message.text:
        bot.send_message(message.chat.id, "@heap_of_1010110 , тебя тут вспоминают", parse_mode='html')
    elif "івсі" in message.text:
        bot.send_message(message.chat.id, "@heap_of_1010110 , тебя тут вспоминают", parse_mode='html')
    elif " бот" in message.text:
        bot.send_message(message.chat.id, "<b>кто, я бот??</b>", parse_mode='html')
    elif "Бот" in message.text:
        bot.send_message(message.chat.id, "<b>ты назвал меня ботом?</b>", parse_mode='html')
    elif "бот " in message.text:
        bot.send_message(message.chat.id, "<b>кто, я бот?</b>", parse_mode='html')
    elif "бани гороскоп" in message.text:
        bot.send_message(message.chat.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='♈ БМ «Оплот»', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='♉ Abrams-X', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='♊ Leopard 2', callback_data='zodiac', parse_mode='html', align="left")
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='♋ САУ «Rak»', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='♌ Löwe', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='♍ FGM-148 Javelin', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='♎ Гаага', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='♏ FV101 «Scorpion»', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='♐️ M142 «HIMARS»', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='♑ Козак-2', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='♒ РК-360МЦ «Нептун»', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='♓ Фрегат «Г.Сагайдачный»', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.chat.id, text='Выбери свой знак зодиака:', reply_markup=keyboard)
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп

        # Отправляем текст в Телеграм
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)