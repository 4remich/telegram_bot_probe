from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(command=['Почати'])
def message_start(message):
    bot.send_message(message.chat.id, 'Вітаю!')


@bot.message_handler(command=['cities'])
def message_city(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

    with open('cities.txt') as file:
        cities = [item.split(',') for item in file]

        for city, link in cities:
            url_button = telebot.types.InlineKeyboardButton(text=city.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send_message(message.chat.id, 'Перелік міст', reply_markup=keyboard)


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://radiation-rate.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
