# Телеграм-бот для погоды.
_С помощью этого телеграмм-бота можно узнать текущую температуру, введя название города, в котором нужно узнать текущую температуру воздуха._
## Инструкция по запуску телеграм-бота: ##
_Зарегистрировать бота с помощью телеграм-бота @BotFather._
 
```git clone https://github.com/NoRIS95/weather_bot.git```
 
```cp .env.template .env```
 
```BOT_TOKEN=<вписать сюда токен тг-бота из п.1>```
 
```python3 -m venv dev_venv```
 
```source ./bin/dev_venv/activate```
 
```pip install -r requirements.txt```
 
### Запуск телеграм-бота ###
 
```python main.py```
