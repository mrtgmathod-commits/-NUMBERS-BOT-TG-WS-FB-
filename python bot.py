import telebot

TOKEN = "8018226164:AAGnhcEigex8LIniGkYWBOui5oXG_LjIq2g"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "স্বাগতম NUMBERS BOT-এ 🥰\n\n"
        "⚠️ কোনো স্প্যাম, স্ক্যাম বা অবৈধ ব্যবহার করবেন না।\n"
        "সঠিকভাবে বট ব্যবহার করুন।"
    )

bot.infinity_polling()
