  
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1685123856:AAE1F2pPUJV-tFizLXE_e5dtlHtKy8LiMx8'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
ciao sono un primo bot creato per prova\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

def echo_message(message):
  if message.text=='ciao':
    bot.reply_to(message,'ciao anche a te')
bot.polling()