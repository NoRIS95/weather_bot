import pygismeteo
import telebot
import requests
from simplejsondb import Database
#
with open("our_token.txt", 'r') as file:
    necess_token = file.readline()

bot= telebot.TeleBot(necess_token)
user_answers = Database('user_answers.json', default=dict())


@bot.message_handler(commands=["start"])
def hello_message(message):
    mess = f'Привет, {message.from_user.first_name}! :) Для того, чтобы узнать температуру воздуха в текущий момент времени, введите название города на русском:'
    user_answers.data[message.from_user.id] = mess
    bot.send_message(message.chat.id, user_answers.data[message.chat.id])


@bot.message_handler()
def temperature(message):
    gm = pygismeteo.Gismeteo()
    search_results = gm.search.by_query(message.text)
    city_id = search_results[0].id
    current = gm.current.by_id(city_id)
    answer = f"Температура в городе {message.text}  на текущий момент времени равна {current.temperature.air.c}"
    user_answers.data[message.from_user.id] = answer
    bot.send_message(message.chat.id, user_answers.data[message.from_user.id])


bot.polling(none_stop= True)

