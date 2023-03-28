import os
import telebot

BotToken="My Token"

bot = telebot.TeleBot(BotToken);

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    f = os.popen(message.text, 'r')
    bot.send_message(message.from_user.id,f.read())

bot.polling(none_stop=True, interval=0)

