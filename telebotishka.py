import telebot
from telebot import types

bot = telebot.TeleBot("7094729383:AAFIvc_Vmk4Nwj1RMTZ2L2lUiC5H6rJ9MM8")
@bot.message_handler(commands = ['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("✨Начнём✨", callback_data = 'GG')
    item2 = types.InlineKeyboardButton('Поддержка📈',url = 'https://www.youtube.com/@Lavartyraider')
    item3 = types.InlineKeyboardButton('🤑Донат🤑', url='https://www.donationalerts.com/r/lavartyyt_official')
    item5 = types.InlineKeyboardButton('купить голду',url='https://t.me/GoblinGold_Bot')
    markup.row(item1,item2,item3,item5)

    bot.send_message(message.chat.id , 'Здравствуйте я бот для помощи в игре в стандофф 2',reply_markup=markup)
@bot.callback_query_handler(func=lambda call : True)
def callback_message(call):
    if call.data == 'GG':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Прострелы", callback_data='prostrel')
        item2 = types.InlineKeyboardButton('Расскид', callback_data='rasskidi')
        item4 = types.InlineKeyboardButton('Подсад', callback_data='podsad')
        item5 = types.InlineKeyboardButton('Назад🔙', callback_data='back')
        markup.row(item1, item2,item4,item5)
       # bot.edit_message_text(call.message.chat.id, call.message.message_id, 'Выбери тип вишки', reply_markup=markup)
        bot.send_message(call.message.chat.id, ' Выбери тип фишки',reply_markup=markup)

        # bot.register_callback_query_handler(call, second_level) ереносит в след функцию
    elif call.data == 'prostrel':
        video = open('media/prostrel.mp4','rb')
        bot.send_video(call.message.chat.id, video)
    elif call.data == 'rasskidi':
        videe = open('media/rsskid0.mp4','rb')
        vider = open('media/raskid1.mp4','rb')
        videq = open('media/gg.mp4','rb')
        videi = open('media/w.mp4','rb')
        bot.send_video(call.message.chat.id, videe)
        bot.send_video(call.message.chat.id, vider)
        bot.send_video(call.message.chat.id, videq)
        bot.send_video(call.message.chat.id, videi)
    elif call.data == 'podsad':
        videe = open('media/podsad.mp4','rb')
        bot.send_video(call.message.chat.id, videe)
        
    
    
        
@bot.message_handler(commands = ['dast'])
def second_level(call):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Прострелы", callback_data='lifehack')
        item2 = types.InlineKeyboardButton('Расскиды', callback_data='lifehack')
        item3 = types.InlineKeyboardButton('Ванвей смоки', callback_data='lifehack')
        item4 = types.InlineKeyboardButton('Подсад', callback_data='podsad')
        item5 = types.InlineKeyboardButton('Назад🔙', callback_data='back')
        markup.row(item1, item2, item3,item4,item5)

        bot.send_message(call.data.message.chat.id, 'Здравствуйте я бот для помощи в игре в стандофф 2',reply_markup=markup)
        if call.data == "back":
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("✨Начнём✨", callback_data='GG')
            item2 = types.InlineKeyboardButton('Поддержка📈', url='https://www.youtube.com/@Lavartyraider')
            item3 = types.InlineKeyboardButton('🤑Донат🤑', url='https://www.donationalerts.com/r/lavartyyt_official')

            item5 = types.InlineKeyboardButton('купить голду',url='https://t.me/GoblinGold_Bot')
            markup.row(item1,item2,item3,item5)

            bot.send_message(message.chat.id, 'Здравствуйте я бот для помощи в игре в стандофф 2', reply_markup=markup)

bot.polling(none_stop=True)
