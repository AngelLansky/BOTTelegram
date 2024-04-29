from telebot import types
from telebot.types import InlineKeyboardMarkup


#Функция меню
def menu(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'menu')

    def menu_callback(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'menu':

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🛍️Сделать заказ', callback_data='order'))
            markup.add(types.InlineKeyboardButton('💰Калькулятор стоимости', callback_data='calcul'))
            markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
            markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', callback_data='question'))
            markup.add(types.InlineKeyboardButton('📲POIZON на iOS', url='https://apps.apple.com/kz/app/得物-有毒的运动-潮流-好物/id1012871328'))
            markup.add(types.InlineKeyboardButton('📲POIZON на Android', url='https://www.anxinapk.com/rj/12201303.html'))
            photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_photo(call.message.chat.id, photo, caption=
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


#Функция калькулятора
def register_handler(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'calcul')

    def calcul(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('👟Летняя обувь', callback_data='summer'))
        markup.add(types.InlineKeyboardButton('🥾Зимняя обувь', callback_data='winter'))
        markup.add(types.InlineKeyboardButton('👕Майки/рубашки/толстовки', callback_data='short'))
        markup.add(types.InlineKeyboardButton('🛍️Парфюм/акс...ры/сумки', callback_data='parph'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
        bot.send_photo(call.message.chat.id, photo, caption=
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


#Функция популярных вопросов
def answer_the_question(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'ask')

    def ask_question(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'ask':

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Будет ли цена дешевле,\n если заказать несколько вещей?', callback_data='no'))
            markup.add(types.InlineKeyboardButton('Сколько времени\n занимает доставка?', callback_data='time'))
            markup.add(types.InlineKeyboardButton('Какая у вас комиссия?', callback_data='kom'))
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id, '📢Ответы на самые популярные вопросы:', parse_mode='html', reply_markup=markup)


#Функция ответов на вопрос цены
def question_no(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'no')

    def check_callback(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📢️Ответы на популярные вопросы', callback_data='ask'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))

        if call.data == 'no':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=
                                  '🛍️Будет ли цена дешевле, если заказть несколько вещей?\n'
                                  '\n'
                                  '❌К сожалению, нет'
                                  , reply_markup=markup
                                  )


#Функция ответов на вопрос доставки
def question_time(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'time')

    def check_callback(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))

        if call.data == 'time':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=
                                  '🚚Сколько времени занимает доставка?\n'
                                  '\n'
                                  'Обычно доставка до России занимает не более 2-ух недель, в редких исключениях когда товар доставляется из других стран доставка может быть увеличена, но об этом мы обязательно предупредим)'
                                  , reply_markup=markup
                                  )


#Функция ответов на вопрос комиссии
def question_kom(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'kom')

    def check_callback_time(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))

        if call.data == 'kom':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=
                                  '🔍Какая у вас комиссия?\n'
                                  '\n'
                                  '🕵️‍♂️Мы не можем раскрыть формулы по которым считаем цену, но так как в Китае есть наш склад, а так же часть команды находится там, то это позволяет нам организовывать быструю доставку и самую низкую цену❤️'
                                  , reply_markup=markup
                                  )


#Функция перенаправки на оператора
def question_to_operator(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'question')

    def question_operator(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
        markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))

        if call.data == 'question':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '😇Друзья, пожалуйста, пишите в поддержку только, если не смогли найти ответы в часто задаваемых вопросах.\n'
                             '\n'
                             '‼ВНИМАНИЕ‼ Поддержка НИКОГДА не просит перевести оплату за заказы в сообщения, все оплаты проходят в автоматическом режиме через БОТ!\n'
                             '\n'
                             'Чтобы начать диалог с оператором пожалуйста нажмите "👨‍💻Задать вопрос" Также мы можем помочь Вам оформить заказ, найти нужные товары на POIZON или TAOBAO. Чтобы воспользоваться этой услугой также нажмите "👨‍💻Задать вопрос"'
                             '      ', reply_markup=markup
                             )


#Функция калькулятора всех товаров
def delivery_calc_summer(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'summer')

    def calc_all_goods(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'summer':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🚚Автомобильная доставка лето', callback_data='auto_summer'))
            markup.add(types.InlineKeyboardButton('✈️Авиа доставка лето', callback_data='avia_summer'))
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )


def delivery_calc_winter(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'winter')

    def calc_all_goods(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'winter':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🚚Автомобильная доставка зима', callback_data='auto_winter'))
            markup.add(types.InlineKeyboardButton('✈️Авиа доставка зима', callback_data='avia_winter'))
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )


def delivery_calc_short(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'short')

    def calc_all_goods(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'short':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🚚Автомобильная доставка', callback_data='auto_short'))
            markup.add(types.InlineKeyboardButton('✈️Авиа доставка', callback_data='avia_short'))
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )


def delivery_calc_parph(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data == 'parph')
    def calc_all_goods(call):

        bot.answer_callback_query(callback_query_id=call.id)

        if call.data == 'parph':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🚚Автомобильная доставка', callback_data='auto_parph'))
            markup.add(types.InlineKeyboardButton('✈️Авиа доставка', callback_data='avia_parph'))
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )


#Функция подсчета стоимости
def calculator_goods_auto_avia(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data)

    def calc_before_delivery(call):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')

        if call.data == 'auto_summer':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_summer_auto)

        elif call.data == 'auto_winter':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_winter_auto)

        elif call.data == 'auto_short':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_short_auto)

        elif call.data == 'auto_parph':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_parph_auto)

        elif call.data == 'avia_summer':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_summer_avia)

        elif call.data == 'avia_winter':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_winter_avia)

        elif call.data == 'avia_short':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_short_avia)

        elif call.data == 'avia_parph':
            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            mess = bot.send_photo(call.message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mess, calculator_parph_avia)

    def calculator_summer_auto(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21.4
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 17.5
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 16.5 + float(variable) * 1.65
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_summer_auto)

    def calculator_summer_avia(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 23.4
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19.5
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18.5 + float(variable) * 1.85
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_summer_avia)

    def calculator_winter_auto(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21.8
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19.4
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 17.9
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 16.9 + float(variable) * 1.69
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_winter_auto)

    def calculator_winter_avia(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 23.8
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21.4
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19.9
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18.9 + float(variable) * 1.89
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_winter_avia)

    def calculator_short_auto(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18.6
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 17.3
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 16.3 + float(variable) * 1.63
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_short_auto)

    def calculator_short_avia(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 23.2
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19.3
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18.3 + float(variable) * 1.83
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_short_avia)

    def calculator_parph_auto(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 21.1
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18.5
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 17.1
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 16.1 + float(variable) * 1.61
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авто доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_parph_auto)

    def calculator_parph_avia(message):

        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        variable = message.text

        try:
            variable = int(variable)

            if 1 <= variable <= 300:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 22.9
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 301 <= variable <= 600:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 20.6
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 601 <= variable <= 900:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 19
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            elif 901 <= variable <= 3000:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                price = float(variable) * 18 + float(variable) * 1.8
                bot.send_message(message.chat.id,
                                 f'💰Итоговая стоимость: {int(price)} руб с учетом доставки до России и страхованием товара\n'
                                 '\n'
                                 'Тип доставки: Авиа доставка'
                                 '\n'
                                 '🚚 Доставка СДЭКом по России до Вашего пункта выдачи оплачивается ОТДЕЛЬНО.',
                                 reply_markup=markup
                                 )

            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('💰Вернуться в калькулятор', callback_data='calcul'))
                markup.add(types.InlineKeyboardButton('👨‍💻Задать вопрос', url='t.me/TovarovedPro'))
                markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
                bot.send_message(message.chat.id,
                                 '🤖Через бота можно заказать товары стоимостью до 3000¥.\n'
                                 'Для заказа на сумму свыше 3000¥, вы можете связаться с оператором👨‍💻, оплата проходит через оператора\n',
                                 reply_markup=markup
                                 )

        except:
            bot.send_message(message.chat.id, 'Неверный ввод, введите число')
            mesg = bot.send_photo(message.chat.id, photo,
                                  'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                                  '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                                  )
            bot.register_next_step_handler(mesg, calculator_parph_avia)


def order_goods(bot):

    @bot.callback_query_handler(func=lambda callback: callback == 'order')

    def order(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('👟Летняя обувь', callback_data='summer_order'))
        markup.add(types.InlineKeyboardButton('🥾Зимняя обувь', callback_data='winter_order'))
        markup.add(types.InlineKeyboardButton('👕Майки/рубашки/толстовки', callback_data='short_order'))
        markup.add(types.InlineKeyboardButton('🛍️Парфюм/акс...ры/сумки', callback_data='parph_order'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))
        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
        bot.send_photo(call.message.chat.id, photo, caption=
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


