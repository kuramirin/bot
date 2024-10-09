from telebot.types import BotCommand

default_commands = [
    BotCommand("start","приветствие"),
     BotCommand("help", "список команд"),
     BotCommand("wiseness","случайная цитата"),
     BotCommand("random_advice", "совет от бота",),
     BotCommand("convert","конвертировать любую валюту в рубли"),
     BotCommand("set_my_currency", "установить целевую валюту", ),
     BotCommand("secret", "only for admin",)
    ]




