import advices
from bot import bot, handle_any_convert_to_many_inline_query
from telebot import types
import currencies

def handle_any_inline_query(query: types.InlineQuery):
    result = advices.prepare_default_result_article(str(query.id))
    results = [result,]
    bot.answer_inline_query(
        inline_query_id = query.id,
        results=results,
        cache_time = 10,)


def handle_convert_query_with_selected_currency(query: types.InlineQuery):
    amount_str, _, currency =query.query.partition(" ")
    amount = int(amount_str)
    target_currencies = currencies.FAVORITE_CURRENCIES

    handle_any_convert_to_many_inline_query(
        query=query,
        amount=amount,
        from_currency=currency,
        target_currencies = target_currencies,)