import telebot
import requests
import datetime

covid_api = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
token = '2075557284:AAFWsq1fyD2HPn5sZKSrsF6vJbgeG_vr4QE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'старт'])
def send_start(message):
    bot.send_message(message.chat.id, 'Hi, I am COVID19-bot')


@bot.message_handler(content_types='text')
def send_data(message):
    covid = requests.get(covid_api.format(country=message.text.title()))
    covid_json = covid.json()
    today = datetime.datetime.now()
    data = f'Количество заболевших коронавирусом в {message.text.title()}: {covid_json["All"]["confirmed"]} на дату: {today.day}-{today.month}-{today.year}'
    bot.send_message(message.chat.id, data)



print('Bot is working')
bot.infinity_polling()
