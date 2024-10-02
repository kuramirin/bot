from telebot.custom_filters import(SimpleCustomFilter,)
from telebot.types import Message
import toki
class IsUserBotAdmin(SimpleCustomFilter):
    key = 'is_bot_admin'

    def check(self, message: Message):
       return message.from_user.id in toki.BOT_ADMIN_USER_IDS