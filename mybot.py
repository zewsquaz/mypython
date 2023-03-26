
import telebot

print("My first telegram bot")

bot = telebot.TeleBot(" my token ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, "Да, "+ message.text)
    print(message.text, type( message.text ))


bot.polling( none_stop = True )


