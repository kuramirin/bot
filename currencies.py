import requests
from datetime import date
from functools import lru_cache
from decimal import Decimal



USD_RUB = 95.25

default_currency_key = "default currency"   

local_currency_key ="local_currency"
CURRENCIES_API_LIST_URL = ("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json")


CURRENCIES_API_URL = ("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency}.json")

ERROR_FETCHING_VALUE = -1
ERROR_CURRENCY_NOT_FOUND = -2
ERROR_CURRENCY_INVALID = -3

FAVORITE_CURRENCIES = [
    "RUB"
    "USD"
    "EUR"
]
DEFAULT_LOCAL_CURRENCY = "RUB"

def fetch_available_currencies():
    response = requests.get(CURRENCIES_API_LIST_URL)
    if response.status_code == 200:
        return response.json()
    return

def is_currency_available(currency: str) -> bool:
    return currency.lower() in fetch_available_currencies()

def fetch_all_available_currencies():
    response = requests.get(CURRENCIES_API_LIST_URL)
    if response.status_code == 200:
        return response.json()
    return{}

@lru_cache(maxsize = 1)
def fetch_available_currencies_for_date(the_date):
    """
    Fetches available. Param the_date is more caching (key)
    
    :param the_date:
    :return:
    """
    print("fetching available currencies for", the_date)
    return fetch_all_available_currencies()

def get_latest_available_currencies():
    today = date.today().isoformat()
    return fetch_available_currencies_for_date(today)


def is_currency_available(currency: str) -> bool:
    return currency.lower() in get_latest_available_currencies()

def get_currency_ratio(from_currency, to_currency):
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()
    url = CURRENCIES_API_URL.format(currency= from_currency)
    response = requests.get(url)
    if response.status_code !=200:
        if response.status_code ==404:
             return ERROR_CURRENCY_NOT_FOUND
        return ERROR_FETCHING_VALUE
    
    
    json_data = response.json(parse_float=Decimal)
    values = json_data[from_currency]
    if to_currency not in values:
        return ERROR_CURRENCY_INVALID
    return values [to_currency]

def get_currencies_ratio(
    from_currency: str,
    to_currencies: list[str],
    ):
    from_currency = from_currency.lower()
    url = CURRENCIES_API_URL.format(currency= from_currency)
    response = requests.get(url)

    json_data = response.json(parse_float=Decimal)
    values = json_data[from_currency]

    result = []
    for currency in to_currencies:
        to_currency = currency.lower()
        if to_currency in values:
           result.append(values[to_currency])
        else:
           result.append(0)
    return result





def get_usd_to_rub_ratio():
    return get_currency_ratio(from_currency = "usd",
        to_currency = "rub" ,)


def get_currencies_name(currency: str, default_to: str = "RUB",):
    if " " in currency:
        currency_from, _, currency_to = currency.partition(" ")
        currency_from = currency_from.strip()
        currency_to = currency_to.strip()
    else:
        currency_from = currency
        currency_to = default_to
    return currency_from, currency_to            