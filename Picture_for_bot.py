import telebot
bot = telebot.TeleBot('5898694887:AAGB4H4swLAMABglTKrOWV3ubRcsixNtZKA')
import random
@bot.message_handler()
#number = random.randint(1,7)
def show_picture(message):
    number = random.randint(1, 7)
    if number == 1 or number == 2:
        photo = open('Catt.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Funny cat')
    elif number == 3 or number == 4:
        photo = open('Tired.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Funny hamster')
    elif number == 5:
        photo = open('Foxx.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Funny fox')
    else:
        photo = open('Tea.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Just true')
