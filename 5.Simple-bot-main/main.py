import telebot
from telebot import types

token = "2119539462:AAGFiJPdMVXWLPWhUxUbAI6T8IodY5cRL8M"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help","/music","/cybersport","/games",)
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n'\
        "Показывать,где можно послушать музыку /music \n"\
        "Показывать,где можно узнать киберспортивные события /cybersport \n"\
        "Показывать,где можно поиграть в игру /games \n"\
        "/start \n")


@bot.message_handler(commands=['music'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тебе сюда - https://music.youtube.com')


@bot.message_handler(commands=['cybersport'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тебе сюда - https://ggscore.com/ru')

@bot.message_handler(commands=['games'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здесь можно поиграть - https://steamcommunity.com')




@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "хочу узнать страницу создателя":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://vk.com/q_u_a_n_t_6_0?')
    if message.text.lower() == "хочу узнать новости":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://www.bbc.com/news/world')
    if message.text.lower() == "хочу узнать спортивные новости и события":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://news.sportbox.ru/?.=')



bot.polling()


