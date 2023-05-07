import pygismeteo
import telebot
from simplejsondb import Database
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
TG_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)
USER_ANSWERS = Database('user_answers.json', default=dict())


@bot.message_handler(commands=["start"])
def hello_message(message):
    mess = f'Привет, {message.from_user.first_name}! :) Для того, чтобы узнать температуру воздуха в текущий момент времени, введите название города на русском:'
    USER_ANSWERS.data[message.from_user.id] = mess
    bot.send_message(message.chat.id, USER_ANSWERS.data[message.chat.id])


@bot.message_handler()
def temperature(message):
    gm = pygismeteo.Gismeteo()
    search_results = gm.search.by_query(message.text)
    city_id = search_results[0].id
    current = gm.current.by_id(city_id)
    answer = f"Температура в городе {message.text}  на текущий момент времени равна {current.temperature.air.c}"
    USER_ANSWERS.data[message.from_user.id] = answer
    bot.send_message(message.chat.id, USER_ANSWERS.data[message.from_user.id])


bot.polling(none_stop= True)

