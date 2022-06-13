import config
import telebot
from pycbrf import ExchangeRates
from datetime import date

today = date.today()

bot = telebot.TeleBot(config.TOKEN)
rates = ExchangeRates(today)

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Привет! Я бот")

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, "Ничем не могу тебе помочь")

@bot.message_handler(commands=["usd"])
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["gbp"])
def usd(message):
	text = "1 Британский фунт ="+str(rates['GBP'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["cny"])
def usd(message):
	text = "1 Китайский Юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["eur"])
def usd(message):
	text = "1 Евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["chf"])
def usd(message):
	text = "1 Швейцарский франк ="+str(rates['CHF'].rate)+"руб."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["czk"])
def usd(message):
	text = "1 Чешская крона ="+str(rates['CZK'].rate)+"руб."
	bot.send_message(message.chat.id, text)

if __name__ == '__main__':
	bot.infinity_polling()