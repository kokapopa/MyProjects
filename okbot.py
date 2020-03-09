import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])

def welcomemessage(message):
    sticker = open('C:/Users/user/PycharmProjects/BOT/start.webp', 'rb')
    mes = 'привяу'
    bot.send_message(message.chat.id,mes)
    bot.send_sticker(message.chat.id,sticker)

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True) #size texta
    item1 = types.KeyboardButton("🍺")
    item2 = types.KeyboardButton("гав")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'ну че {0.first_name}, все ок?\nя кст <b>{1.first_name}</b>'.format(message.from_user,
                                                                                                    bot.get_me()),
                 parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])

def replymessage(message):
    if message.text == "🍺":
            bot.send_message(message.chat.id, "пасиб бро")
    elif message.text == "гав":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True) #size texta
        item1 = types.KeyboardButton("да")
        item2 = types.KeyboardButton("не")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'блин ты похлду не ок\nпогоыорим об этом?' .format(message.from_user,
                                                                                                    bot.get_me()),
        parse_mode='html', reply_markup=markup)
    elif message.text == "да":
        bot.send_message(message.chat.id, "ну, че такое?")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # size texta
        item1 = types.KeyboardButton("хош")
        item2 = types.KeyboardButton("не")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'ок, мне на самом деле все равно, че у тебя случилось, своих '
                                          'проблем хватает понимаешь да\nно я могу попробовать сделать так,'
                                          'чтобы тебе стало легче, хош?'.format(message.from_user,
                                                                                        bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    elif message.text == 'не':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # size texta
        item1 = types.KeyboardButton("🍺")
        item2 = types.KeyboardButton("гав")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'ok'.format(message.from_user,
                                                            bot.get_me()),
                         parse_mode='html', reply_markup=markup)
    elif message.text == 'хош':
        sticker1 = open('C:/Users/user/PycharmProjects/BOT/ok.webp', 'rb')
        keyboard = types.ReplyKeyboardRemove()
        bot.send_sticker(message.chat.id, sticker1)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="уау", url="https://asoftmurmur.com/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'полный расслабон', reply_markup=keyboard)


    else: bot.send_message(message.chat.id, 'где мое пиво')



bot.polling(none_stop=True)