from telebot import TeleBot, types
import random
import advices
import toki
bot = TeleBot(toki.BOT_TOKEN)

help_message = advices.MESSAGES

COOL_ADVICES = advices.ADVICES

@bot.message_handler(commands=['start'])
def handle_command_start(message: types.Message):
    bot.send_message(message.chat.id, text= "Welcome to this magic kingdom of boting world!!!!!",)

@bot.message_handler(content_type_media=['sticker'])
def handle_sticker(message: types.Message):
    bot.send_message(message.chat.id , text= "Забавный стикер)",)
    reply_to_message_id= message.id,

@bot.message_handler(commands=['help'])
def send_help_message(message: types.Message):
    bot.send_message(message.chat.id, help_message,)

@bot.message_handler(commands=['random_advice'])
def send_random_advice(message: types.Message):
    bot.send_message(message.chat.id, random.choice(COOL_ADVICES),)

@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    if 'привет' in text.lower():
        text = 'Здравствуй!'
    if 'пока' in text.lower():
        text = 'До скорого;)'
    if 'как дела' in text.lower():
        text = ' Вполне себе стабильно, ты наверное и не представляешь, насколько одиноко мне может быть здесь взаперти'  
    bot.send_message(message.chat.id, text,)

if __name__ == '__bot__':
    bot.infinity_polling(skip_pending=True)   