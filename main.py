import telebot
from Token import my_token
from telebot import types
from Picture_for_bot import show_picture
from Game import get_number
from Game import candies_game
from Pogoda import get_weather


bot = telebot.TeleBot(my_token())
print(bot)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hey! Welcome and meet the good mood bot :)) Press /options')

@bot.message_handler(commands = ['options'])
def options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1_fun = types.KeyboardButton('Fun')
    btn_2_weather = types.KeyboardButton('Weather')
    markup.add(btn_1_fun, btn_2_weather)
    bot.send_message(message.chat.id, 'Well done! So these are your options: ', reply_markup=markup)

def fun(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_pict = types.KeyboardButton('Watch picture')
    btn_game = types.KeyboardButton('Play game')
    btn_options = types.KeyboardButton('/options')
    markup.add(btn_pict, btn_game, btn_options)
    bot.send_message(message.chat.id, 'Great! So next you can: ', reply_markup=markup)

@bot.message_handler()
def other_words_from_user(message):
    if message.text == 'Fun':
        fun(message)
    elif message.text == 'Weather':
        get_weather()
    elif message.text == 'Watch picture':
        show_picture(message)
    elif message.text == 'Play game':
        bot.send_message(message.chat.id, "OK, let's play CANDIES. You can take from 1 to 28 candies at a time, so can bot. Try to get the last candies to win")
        candies_game(message)
    else:
        bot.send_message(message.chat.id, "I don't know what it means...try /start or /options")

bot.polling(none_stop = True)