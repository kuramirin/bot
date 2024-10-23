from telebot.types import BotCommand

default_commands = [
    BotCommand("start","приветствие"),
     BotCommand("help", "список команд"),
     BotCommand("survey", "минизнакомство"),
     BotCommand("usd_to_rub", "конвертация из доллара в рубль"),
     BotCommand("wiseness","случайная цитата"),
     BotCommand("random_advice", "совет от бота",),
     BotCommand("convert","конвертировать любую валюту в рубли"),
     BotCommand("set_my_currency", "установить целевую валюту", ),
     BotCommand("art", "моя случайная картинка"),
     BotCommand("media", "my social media"),
     BotCommand("secret", "only for admin",),
    ]




