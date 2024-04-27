from telebot import types


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
        photo = open('Снимок экрана 2024-03-25 в 15.48.00.png', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('📢Ответы на популярные вопросы', callback_data='ask'))
        markup.add(types.InlineKeyboardButton('❤️Меню', callback_data='menu'))

        if call.data == 'kom':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=
                                  '🔍Какая у вас комиссия?\n'
                                  '\n'
                                  '🕵️‍♂️Мы не можем раскрыть формулы по которым считаем цену, но так как в Китае есть наш склад, а так же часть команды находится там, что позволяет нам организовывать быструю доставку и самую низкую цену❤️'
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
def delivery_calc(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data)

    def calc_rub(call):

        bot.answer_callback_query(callback_query_id=call.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🚚Автомобильная доставка', callback_data='car'))
        markup.add(types.InlineKeyboardButton('✈️Авиа доставка', callback_data='avia'))

        if call.data == 'summer':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )

        elif call.data == 'winter':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )

        elif call.data == 'short':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )

        elif call.data == 'parph':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             '\n'
                             '📦Выберите способ доставки:\n'
                             '\n'
                             , reply_markup=markup
                             )


#Функция подсчета стоимости
def calculator_all_goods(bot):

    @bot.callback_query_handler(func=lambda callback: callback.data)

    def calc_before_delivery(call):

        if call.data == 'car':

            bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup='')
            bot.send_message(call.message.chat.id,
                             'Напишите стоимость товара в юанях (зачеркнутая цена)\n'
                             '⚠⚠ Если зачеркнутой цены нет, то напишите обычную.'
                             )

        elif call.data == 'avia':

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='ghfg;lf')
