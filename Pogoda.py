import requests
import telebot
bot = telebot.TeleBot('5898694887:AAGB4H4swLAMABglTKrOWV3ubRcsixNtZKA')
@bot.message_handler()
def ask_city(message):
    global city
    city = bot.send_message(message.chat.id, 'Enter the city: ')
    bot.register_next_step_handler(city, get_weather)
def get_weather (city):
    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5ad7b8fca6310aff7d3bdd2d7d6a2631&units=metric")
    data = r.json()
    bot.send_message(message.chat.id, f"It is {data['main']['temp']} in {city}, \
    it feels like {data['main']['feels_like']}. Pressure is {data['main']['pressure']}. Wind speed is {data['wind']['speed']}.")

# city = input("Enter city: ")
# r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5ad7b8fca6310aff7d3bdd2d7d6a2631&units=metric")
# data = r.json()
# print(data)
# print(f"It is {data['main']['temp']} in {city}, \
# it feels like {data['main']['feels_like']}. \
# Pressure is {data['main']['pressure']}. \
# Wind speed is {data['wind']['speed']}.")

