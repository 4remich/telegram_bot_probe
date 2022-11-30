from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_hundler(command=['start'])
def message_start(massage):
    bot.send_message(message.chat.id, 'hello!')

@bot.message_hundler(command=['city'])
def message_city(massage):
    keyboard = telebot.types.InlineKeyboardMarkup(raw_width=1)

    with open('city') as file:
        city = [item.split('') for item in file]

        for title. link in city:
            url_button = telebot.types.InlineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send_message.chat.id, 'list of cities', reply_markup=keyboard)


@app.route('/' + TOKEN, methods=[POST])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf8"))])
    return "Python Telegram Bot 30-01-2022", 200

@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='***') + TOKEN)
    return "Python Telegram Bot 30-01-2022", 200

if __name__ == '__name__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
