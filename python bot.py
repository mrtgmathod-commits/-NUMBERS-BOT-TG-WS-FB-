import telebot

TOKEN = "8018226164:AAGnhcEigex8LIniGkYWBOui5oXG_LjIq2g"
bot = telebot.TeleBot(8018226164:AAGnhcEigex8LIniGkYWBOui5oXG_LjIq2g)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Welcome to NUMBERS BOT\n\n"
        "⚠️ No spam, no scam, no illegal use.\n"
        "Use this bot responsibly."
    )

bot.infinity_polling()
