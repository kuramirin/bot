from telebot import types


def is_query_only_digits(query:types.InlineQuery):
    if query and query.query:
        return query.query.isdigit()
    return False