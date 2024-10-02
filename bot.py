from telebot import TeleBot, types
from telebot import custom_filters
from telebot import formatting
import random
import advices
import toki
import myfilt
import os
from os import listdir
bot = TeleBot(toki.BOT_TOKEN)
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextContainsFilter())
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(myfilt.IsUserBotAdmin())

help_message = advices.MESSAGES
COOL_ADVICES = advices.ADVICES
COOL_CYTATES = advices.CYTATES
#images = os.listdir(r"C:\Users\amirk\OneDrive\Рабочий стол\cartinka")


def kva_in_caption(message: types.Message):
    return message.caption and 'ква' in message.caption.lower()

def hi_in_text(message: types.Message):
    return message.text and "привет"  in message.text.lower()

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message: types.Message):
    bot.send_sticker(chat_id=message.chat.id, sticker=message.sticker.file_id,)
   # bot.send_message(message.chat.id , text= "Забавный стикер)", reply_to_message_id= message.id,)#
    
@bot.message_handler( is_reply = True)
def handle_forwarded_text(message: types.Message):
    bot.send_message(message.chat.id, toki.dont_forward_commands,)

@bot.message_handler(commands=['start'])
def handle_command_start(message: types.Message):
    bot.send_sticker(message.chat.id, sticker= "CAACAgIAAxkBAAEM561m_BTCrYQKog5CBkhXDTcYaoSJ0gACBQADwDZPE_lqX5qCa011NgQ",)
    #bot.send_sticker(message.chat.id, sticker=message.sticker.file_unique_id: str,)#
    bot.send_message(message.chat.id, text= "Привет! Я бот. Я еще многого не умею, но знаю много цитат, советов, и шуток. Рад познакомится)",)
    
@bot.message_handler(commands =["chat_id"])
def handle_chat_id_request(message: types.Message):
    text = f"Айди чата: {message.chat.id}"
    bot.send_message(message.chat.id, text,)

@bot.message_handler(commands=['random_advice'])
def send_random_advice(message: types.Message):
    bot.send_message(message.chat.id, formatting.hspoiler(random.choice(COOL_ADVICES)),parse_mode = 'HTML',)

@bot.message_handler(commands=['wiseness'])
def send_random_advice(message: types.Message):
   # bot.send_photo(message.chat.id, img = random.choice(images),)
    bot.send_message(message.chat.id, random.choice(COOL_CYTATES), parse_mode = 'HTML',)
    
@bot.message_handler(commands = ["secret"], is_bot_admin = True)
def handle_admin_secret(message: types.Message):
    bot.send_message(message.chat.id, toki.secret_message_for_admin,)

@bot.message_handler(commands = ["secret"], is_bot_admin = False)
def handle_not_admin_secret(message: types.Message):
    bot.send_message(message.chat.id, toki.secret_message_not_for_admin,)

@bot.message_handler(commands=['help'])
def send_help_message(message: types.Message):
    bot.send_message(message.chat.id, help_message,)

@bot.message_handler(commands = ["joke"])
def send_joke_message(message: types.Message):
    bot.send_message(message.chat.id, formatting.hcite(advices.get_random_joke_text), parse_mode = "HTML",)

@bot.message_handler(commands = ["md"])
def send_markdown_message(message: types.Message):
    bot.send_message(message.chat.id, toki.md, parse_mode = 'MarkdownV2',)
    
@bot.message_handler(commands = ["html"])
def send_html_message(message: types.Message):
    bot.send_message(message.chat.id, toki.html_text, parse_mode = 'HTML',)    

@bot.message_handler(commands=['kva'])
def send_frogs_message(message: types.Message):
    bot.send_photo(message.chat.id, toki.FROGS_PIC,)

bot.message_handler()
def copy_incoming_message(message: types.Message):
    #if message.entities:
       ###print("message entities:")
        ###for entity in message.entities:
           # print(entity)
    bot.copy_message(message.chat.id, from_chat_id = message.chat.id, message_id = message.id,)

@bot.message_handler(content_types=['photo'])
def handle_photo(message: types.Message):
    if kva_in_caption(message):
        photo_file_id = toki.FROGS_PIC
    else: 
        photo_file_id = message.photo[-1].file_id
    #bot.send_photo(message.chat.id, photo = photo_file_id, reply_to_message_id = message.id,)
    bot.send_message(message.chat.id, text = formatting.mspoiler('Супер картинка!'),parse_mode = "MarkdownV2", reply_to_message_id= message.id,)

#images.remove(img)

@bot.message_handler(func= hi_in_text)
def handle_hi_message(message: types.Message):
    bot.send_message(message.chat.id, "Здравствуй!",)

@bot.message_handler(text = custom_filters.TextFilter(contains = ['погода'], ignore_case = True,))
def handle_weather_request(message: types.Message):
    bot.send_message(message.chat.id, "Да, сегодня замечательная погода",)

@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    text_lower = text.lower()
    if 'пока' in text.lower():
        text = 'До скорого;)'
    if 'как дела' in text.lower():
        text = ' Вполне себе стабильно, ты наверное и не представляешь, насколько одиноко мне может быть здесь взаперти'  
    bot.send_message(message.chat.id, text,entities= message.entities,)


bot.polling(non_stop = True)