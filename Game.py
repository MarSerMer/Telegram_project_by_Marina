import telebot
bot = telebot.TeleBot('5898694887:AAGB4H4swLAMABglTKrOWV3ubRcsixNtZKA')
import  random
from telebot import types

bunch_of_candies = 100
count = 1
@bot.message_handler(content_types=['text'])
def candies_game(message):
    global bunch_of_candies
    global count
    while bunch_of_candies > 28:
        if count % 2 == True:  # человек будет начинать
            ask_num = bot.send_message(message.chat.id, 'Enter how many sweets you take (from 1 to 28)' )
            bot.register_next_step_handler(ask_num, get_number(ask_num))
            n = get_number(ask_num)
            bunch_of_candies -= n
            count += 1
            bot.send_message(message.chat.id, f'Candies left: {bunch_of_candies}')
        else:  # это блок для четного хода, в данном случае это bot
            number = random.randint(1, 28)
            bot.send_message(message.chat.id, 'Now i take candies.')
            bot.send_message(message.chat.id, f'I take {number} candies')
            # print('Computer takes', number, 'candies. ')
            bunch_of_candies -= number
            count += 1
            bot.send_message(message.chat.id, f'Candies left: {bunch_of_candies}')
            # print('Candies left: ', bunch_of_candies)

    if count % 2 == False:
        bot.send_message(message.chat.id, 'YOU WIN!! CONGRATULATIONS!')
        # print('YOU WIN!! CONGRATULATIONS!')
    else:
        bot.send_message(message.chat.id, 'Bot wins ))')
        # print('Bot wins')


def get_number(message):
    global n
    n = message.text
    return n