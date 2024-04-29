import telebot
from telebot import types, TeleBot
import utils
from config import API_KEY


bot: TeleBot = telebot.TeleBot(API_KEY)


#Обработка команды старт
@bot.message_handler(commands=['start'])

def start_message(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🛍️Сделать заказ', callback_data='order'))
    markup.add(types.InlineKeyboardButton('💰Калькулятор стоимости', callback_data='calcul'))
    markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
    markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', callback_data='question'))
    markup.add(types.InlineKeyboardButton('📲POIZON на iOS', url='https://apps.apple.com/kz/app/得物-有毒的运动-潮流-好物/id1012871328'))
    markup.add(types.InlineKeyboardButton('📲POIZON на Android', url='https://www.anxinapk.com/rj/12201303.html'))
    photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
    bot.send_photo(message.chat.id, photo, caption=
                   '\n'
                   '👋Добро Пожаловать в бот группы TovarovedPRO! \n'
                   '\n'
                   'Наша группа поможет выкупить товары с ЛЮБЫХ китайских площадок, например:\n'
                   '1️⃣POIZON (DEWU)\n'
                   '2️⃣taobao.com\n'
                   '3️⃣и другие...\n'
                   '\n'
                   '⛔Все заказы и оплата производятся ТОЛЬКО В БОТЕ. Мы не принимаем оплату в личных сообщениях⛔\n'
                   '    ', parse_mode='html', reply_markup=markup
                   )


#Обработка команды помощь
@bot.message_handler(commands=['help'])

def help(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Будет ли цена дешевле,\n если заказать несколько вещей?', callback_data='no'))
    markup.add(types.InlineKeyboardButton('Сколько времени\n занимает доставка?', callback_data='time'))
    markup.add(types.InlineKeyboardButton('Какая у вас комиссия?', callback_data='kom'))
    bot.send_message(message.chat.id, '📢Ответы на самые популярные вопросы:', parse_mode='html', reply_markup=markup)


#Меню калькулятора
@bot.message_handler(commands=['calc'])

def calc(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👟Летняя обувь', callback_data='summer'))
    markup.add(types.InlineKeyboardButton('🥾Зимняя обувь', callback_data='winter'))
    markup.add(types.InlineKeyboardButton('👕Майки/рубашки/толстовки', callback_data='short'))
    markup.add(types.InlineKeyboardButton('🛍️Парфюм/акс...ры/сумки', callback_data='parph'))
    markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
    photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
    bot.send_photo(message.chat.id, photo, caption=
                   '\n'
                   'В нашем калькуляторе Вы можете сделать рассчет стоимости товара с доставкой до России\n'
                   '\n'
                   'В калькуляторе указывайте цены в юанях <b><u>Только</u></b> по <s>зачернутому</s> ценнику. Если его нет, то укажите обычную цену.\n'
                   '\n'
                   'Товары с ≈ <b>НЕ ВЫКУПАЕМ</b>\n'
                   '\n'
                   '⛔ Если Ваш товар стоит больше 1500 юаней, то к стоимости товара следует прибавлять 10% в юанях. 10% взымается за страхование товара, в случае утери или кражи возврат 100% стоимости товара. ⛔\n'
                   '    ', parse_mode='html', reply_markup=markup
                   )


#Обработка всех неизвестных запросов
@bot.message_handler(content_types=['text'])

def send_text(message):

    global keyId

    bot.send_message(message.chat.id, 'Я еще не научился понимать такие команды🤖')


#Заказ написать позже!!!
@bot.callback_query_handler(func=lambda callback: callback.data == 'order')

def check_callback(call):

    bot.answer_callback_query(callback_query_id=call.id)
    photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')

    if call.data == 'order':

        bot.register_next_step_handler()


#Функция меню
utils.menu(bot)


#Обработка заказа


#Обработка запроса калькулятора
utils.register_handler(bot)


#Обработка стартовых ответов на вопросы
utils.answer_the_question(bot)


#Ответы на популярные вопросы
utils.question_no(bot)

utils.question_time(bot)

utils.question_kom(bot)


#Вопрос оператору
utils.question_to_operator(bot)


#Калькулятор стоимости доставки
utils.calculator_goods_auto(bot)


#Калькулятор
utils.delivery_calc_summer(bot)





bot.infinity_polling()