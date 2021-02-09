
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = '1459713391:AAHymmVVZxIxVYpoExjJFTR7tx9kSQolYCI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Ciao, questo è il progetto PCTO, classe 4BT-i, A.S 2020/2021""")
    bot.reply_to(message, """progetto di Coman E., Franturi M. e Vignoli M.""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

def echo_message(message):
  if message.text=='Ciao':
    bot.reply_to(message,'ciao ancha te')


bot.polling()
