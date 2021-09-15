import telebot
import parser

token = ''
kbot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'go'])

def start_handler(message):
    kbot.send_message(message.chat.id, 'Hello world, bleat')
bot.polling