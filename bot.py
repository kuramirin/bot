from telebot import TeleBot, types
from telebot import custom_filters
from telebot import formatting
from telebot import util
from commands import default_commands
from currencies import default_currency_key
from datetime import timedelta
import currencies
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
    bot.send_sticker(message.chat.id, sticker= "CAACAgIAAxkBAAEM6adm_lpKMwuXg8v5Z9Aao9wPXP2SsQACMTQAAugboErSr6fEZiaivDYE",)
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

#@bot.message_handler(commands = ["joke"])
#def send_joke_message(message: types.Message):
    #bot.send_message(message.chat.id, formatting.hcite(advices.get_random_joke_text), parse_mode = "HTML",)

@bot.message_handler(commands = ["md"])
def send_markdown_message(message: types.Message):
    bot.send_message(message.chat.id, toki.md, parse_mode = 'MarkdownV2',)
    
@bot.message_handler(commands = ["html"])
def send_html_message(message: types.Message):
    bot.send_message(message.chat.id, toki.html_text, parse_mode = 'HTML',)    

@bot.message_handler(commands=['kva'])
def send_frogs_message(message: types.Message):
    bot.send_photo(message.chat.id, toki.FROGS_PIC,)


def has_no_command_arguments(message: types.Message):
    return not util.extract_arguments(message.text)


@bot.message_handler(commands=["convert"], func = has_no_command_arguments)
def handle_cvt_currency_no_arguments(message: types.Message):
        bot.send_message(message.chat.id, advices.cvt_how_to, parse_mode = "HTML")
        
    
@bot.message_handler(commands=["convert"],)
def handle_cvt_currency(message: types.Message):
    arguments = util.extract_arguments(message.text)
    amount, _, currency = arguments.partition(" ")

    if  not amount.isdigit():
        error_text = formatting.format_text(advices.invalid_argument, formatting.hcode(arguments),advices.cvt_how_to,)
        bot.end_message(message.chat.id, error_text,parse_mode = 'HTML')
        return
    currency = currency.strip()
    default_currency = "RUB"

    user_data = bot.current_states.get_data(message.chat.id, user_id = message.from_user.id)

    if user_data and default_currency_key in user_data:
        default_currency = user_data[default_currency_key]

    currency_from, currency_to = currencies.get_currencies_name(currency=currency, default_to = default_currency)

    ratio = currencies.get_currency_ratio(from_currency=currency_from, to_currency = currency_to,)

    if ratio == currencies.ERROR_FETCHING_VALUE:
        bot.send_message(message.chat.id, advices.error_fetching_currencies_text,)
        return
    
    if ratio in {currencies.ERROR_CURRENCY_NOT_FOUND, currencies.ERROR_CURRENCY_INVALID}:
        bad_currency = currency_from
        bot.send_message(message.chat.id, advices.error_no_such_currency.format(currency = formatting.hcode(bad_currency)), parse_mode = "HTML",) 
        return   
    
    from_amount = int(amount)
    result_amount = from_amount * ratio
    bot.send_message(message.chat.id, advices.format_currency_convert_message(from_currency = currency_from,to_currency = currency_to,from_amount = from_amount, to_amount = result_amount,), parse_mode = "HTML")
    bot.send_sticker(message.chat.id, sticker = 'CAACAgIAAxkBAAEM60NnAAEnV4YEU-b9MYTD4e6ZEK4RTKsAAn89AAItySlKdrcmTxVTXBc2BA',)

@bot.message_handler(commands= ["set_my_currency"], func= has_no_command_arguments)
def handle_no_arg_to_set_my_currency(message: types.Message):
    bot.send_message(message.chat.id, text=advices.set_my_currency_help_message, parse_mode = "HTML",)




@bot.message_handler(commands= ["set_my_currency"],)
def handle_set_my_currency(message: types.Message):   
   currency = util.extract_arguments(message. text)
   if not currencies.is_currency_available(currency or ""):
       bot.send_message(message.chat.id, advices.error_no_such_currency.format(currency = formatting.hcode(currency)), parse_mode = "HTML",)
       return
   if bot.get_state(
       user_id = message.from_user.id, chat_id = message.chat.id,
   )is None: bot.set_state(user_id = message.from_user.id, chat_id = message.chat.id, state = 0)

   bot.add_data(user_id=message.from_user.id, chat_id =  message.chat.id, **{currencies.default_currency_key: currency},)
   bot.send_message(message.chat.id, advices.set_my_currency_success_message.format(currency = formatting.hcode(currency)), parse_mode= "HTML",)

#def copy_incoming_message(message: types.Message):
    #if message.entities:
       ###print("message entities:")
        ###for entity in message.entities:
           # print(entity)
    #bot.copy_message(message.chat.id, from_chat_id = message.chat.id, message_id = message.id,)

@bot.message_handler(content_types=['photo'])
def handle_photo(message: types.Message):
    if kva_in_caption(message):
        photo_file_id = toki.FROGS_PIC
    else: 
        photo_file_id = message.photo[-1].file_id
    #bot.send_photo(message.chat.id, photo = photo_file_id, reply_to_message_id = message.id,)
    bot.send_message(message.chat.id, text = formatting.mspoiler('Супер картинка!'),parse_mode = "MarkdownV2", reply_to_message_id= message.id,)

#images.remove(img)
@bot.message_handler(commands = ["usd_to_rub"])
def convert_usd_to_rub(message: types.Message):
    arguments = util.extract_arguments(message. text)
    if not arguments:
        bot.send_message(message.chat.id, advices.how_to_convert_usd_rub, parse_mode = "HTML")
        return
    if not arguments.isdigit():
        text = formatting.format_text(formatting.format_text(advices. invalid_argument,formatting.hcode(arguments)), advices.how_to_convert_usd_rub,)
        bot.send_message(message.chat.id, text, parse_mode = "HTML",)
        return
    
    
    usd_amount = int(arguments)
    ratio = currencies.get_usd_to_rub_ratio()
    rub_amount = usd_amount * ratio

    bot.send_message(message.chat.id, advices.format_convert_usd_to_rub(usd_amount=usd_amount,rub_amount=rub_amount,), parse_mode = "HTML",)

def shedule_func_2(message: types.Message):
    bot.send_message(message.chat.id, random.choice(advices.good_morning),)



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


def any_query(query: types.InlineQuery):
    print(query)
    return True

@bot.inline_handler(func = any_query)
def handle_any_inline_query(query: types.InlineQuery):
    pass


bot.set_my_commands(default_commands)
bot.enable_saving_states
bot.infinity_polling()