tmp_list = []

import telebot
import os

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        tmp_list.append(message.from_user.first_name)
        bot.reply_to(message, str(tmp_list))

# ---------------- local testing ----------------
if __name__ == '__main__':
    bot.infinity_polling()