import pygismeteo
import telebot
from simplejsondb import Database
import os
from dotenv import load_dotenv, find_dotenv
import enum
load_dotenv()
TG_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)
USER_CONDITIONS = Database('user_states.json', default=dict())
gm = pygismeteo.Gismeteo()
class StatusDialog(enum.Enum):
    STATUS_OF_GREEЕTINGS = 1
    STATUS_OF_ASK_CITY = 2


@bot.message_handler(commands=["start"])
def hello_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! :) Для того, чтобы узнать температуру воздуха в текущий момент времени, введите название города на русском:')
    USER_CONDITIONS.data[message.from_user.id] = StatusDialog.STATUS_OF_GREEЕTINGS.value


@bot.message_handler()
def temperature(message):
    if USER_CONDITIONS.data[message.from_user.id] == 1:
        search_results = gm.search.by_query(message.text)
        city_id = search_results[0].id
        current_temperature = gm.current.by_id(city_id)
        bot.send_message(message.chat.id, f"Температура в городе {message.text}  на текущий момент времени равна {current_temperature.temperature.air.c}")
        USER_CONDITIONS.data[message.from_user.id] = StatusDialog.STATUS_OF_ASK_CITY.value
    else:
        search_results = gm.search.by_query(message.text)
        city_id = search_results[0].id
        current_temperature = gm.current.by_id(city_id)
        bot.send_message(message.chat.id, f"Температура в городе {message.text}  на текущий момент времени равна {current_temperature.temperature.air.c}")
        USER_CONDITIONS.data[message.from_user.id] = StatusDialog.STATUS_OF_ASK_CITY.value

bot.polling(none_stop= True)

