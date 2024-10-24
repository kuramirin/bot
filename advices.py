import requests
from telebot import formatting, types

ADVICES = ["Пойми, что тебе по-настоящему нравится. Это и самое главное, и самое сложное. Золотое правило гласит – делай то, что доставляет тебе истинное удовольствие, и тогда ты станешь намного счастливее. Но надо быть готовым к тому, что поиск своего пути – это марафон, который может продолжаться много (десятков?) лет. ",
           "Откажись от мусора, который ты ешь, пьешь и куришь каждый день. Никаких секретов и хитрых диет – просто натуральная пища, фрукты, овощи, вода. Не надо становиться вегетарианцем и полностью завязывать с выпивкой, - достаточно лишь максимально ограничить сахар, муку, кофе, алкоголь и всю пластмассовую еду. ",
           "Учи иностранные языки. Это нереально расширит глубину восприятия мира и откроет невиданные перспективы для обучения, развития и карьерного роста. Русскоязычных пользователей интернета 60 миллионов. Англоязычных – миллиард. Центр прогресса сейчас находится по другую сторону границы, в том числе языковой. Знание английского – это уже не просто прихоть интеллигентов, а жизненная необходимость. ",
           "Читай книги. Примерный круг – твоя профессиональная область, история, естествознание, личностный рост, социология, психология, биографии, качественная художественная литература. Нет времени читать потому, что ездишь за рулем – слушай аудиокниги. Золотое правило – читай/слушай как минимум одну книгу в неделю. Это 50 книг в год, которые перевернут твою жизнь. ",
           "Проводи с толком каждые свои выходные. Сходи в музей, на выставку, займись спортом, съезди за город, прыгни с парашютом, навести родственников, сходи на хороший фильм. Расширяй зону контакта с миром. Когда уже все объездишь и обойдешь, бери с собой друзей и рассказывай им то, что знаешь. Главное – не сиди на месте. Чем больше впечатлений ты пропустишь через себя, тем интереснее будет жизнь, и тем лучше ты будешь разбираться в вещах и явлениях. ",
           "Начни вести блог или обычный дневник. Все равно о чем. Не беда, что ты не обладаешь красноречием и у тебя будет не больше 10 читателей. Главное, что на его страницах ты сможешь думать и рассуждать. А если ты просто регулярно пишешь о том, что ты любишь, читатели обязательно придут. ",
           " Ставь цели. Фиксируй их на бумаге, в Word’е или блоге. Главное, чтобы они были четкими, понятными и измеримыми. Если поставишь цель, то можешь ее или достигнуть, или нет. Если не поставишь, то вариантов достижения нет вообще. ",
           "Научись печатать на клавиатуре вслепую – не уметь этого в 21 веке все равно, что не уметь писать ручкой в 20-м. Время - это одно из немногих сокровищ, которые у тебя есть, и печатать ты должен уметь почти так же быстро, как и думать. А думать ты должен не о том, где находится нужная буква, а о том, что ты пишешь.",
           "Оседлай время. Научись управлять своими делами так, чтобы они работали почти без твоего участия. Для начала почитай Аллена (Getting Things Done) или Глеба Архангельского. Принимай решения быстро, действуй незамедлительно, не откладывай «на потом». Все дела либо делай, либо делегируй кому-то. Старайся, чтобы мяч никогда не задерживался на твоей стороне. Запиши на листе все «долгоиграющие» дела, которые до сих пор не сделаны и мешают тебе жить. Переосмысли, нужны ли они тебе. Сделай то, что осталось, в течение нескольких дней, и ты почувствуешь неимоверную легкость. ",
           "Откажись от компьютерных игр, бесцельного сидения в социальных сетях и тупого серфинга в интернете.Минимизируй общенией в соцсетях (вплоть до оптимизации - оставь всего один аккаунт). Уничтожь в квартире телевизионную антенну. Чтобы не тянуло постоянно проверять электронную почту, установить агент, который будет сообщать тебе о входящих сообщениях (в т.ч. на мобильный). ",
           " Перестань читать новости. Все равно о ключевых событиях будут говорить все вокруг, а дополнительная шумовая информация не приводит к улучшению качества принятия решений. ",
           "Научись рано вставать. Парадокс в том, что в ранние часы ты всегда успеваешь больше, чем в вечерние. Если летом на выходных ты выедешь из Москвы в 7 утра, то к 10 ты уже будешь в Ярославле. Если выедешь в 10, то будешь там в лучшем случае к обеду. То же самое и с шоппингом на выходных. Человеку достаточно 7 часов сна, при условии качественной физической нагрузки и нормальном питании. ",
           "Старайся окружать себя порядочными, честными, открытыми умными и успешными людьми. Мы – это наше окружение, у которого мы учимся всему, что знаем. Проводи больше времени с людьми, которых ты уважаешь и у которых можно чему-нибудь научиться (особенно важно, чтобы в категорию таких людей попадало твое начальство). Соответственно, старайся минимизировать общение с людьми негативными, унылыми, пессимистичными и злыми. Чтобы стать выше, ты должен стремиться вверх, и наличие рядом людей, до которых хочется расти, само по себе станет отличным стимулом. ",
           "Используй каждый момент времени и каждого человека для того, чтобы узнать что-то новое. Если жизнь сводит тебя с профессионалом в любой области, попытайся понять, что составляет суть его работы, каковы его мотивации и цели. Учись задавать правильные вопросы – даже таксист может стать бесценным источником информации. ",
           "Купи фотоаппарат (можно самый простой) и пытайся ловить красоту мира. Когда у тебя получится, ты будешь помнить свои путешествия не только по смутным впечатлениям, но и по красивым фотографиям, которые ты привез с собой. В качестве альтернативы - попробуй рисовать, петь, танцевать, лепить, проектировать. То есть делай то, что заставит тебя взглянуть на мир иными глазами. ",
           "Займись спортом. Не обязательно ходить в фитнес-клуб, где тусуются качки, пикаперы, бальзаковские дамы и фрики. Йога, скалолазание, велосипед, турник, брусья, футбол, бег, плиометрика, плавание, функциональные тренировки – лучшие друзья человека, который хочет вернуть тонус телу и получить всплеск эндорфинов. И забудь о том, что такое лифт – если надо пройти пешком меньше 10 этажей, используй ноги. Всего за 3 месяца методичной работы над собой можно изменить тело почти до неузнаваемости. ",
           "Делай необычные вещи. Сходи туда, где ни разу не был, езди на работу другой дорогой, разберись в проблеме, о которой вообще ничего не знаешь. Выходи из своей «зоны комфорта», расширяй знания и кругозор. Переставь дома мебель (и делай это примерно раз в год), измени внешность, прическу, имидж. ",
           "Отдавай больше, чем берешь. Делись знаниями, опытом и идеями. Человек, который не только берет, но и делится, неимоверно притягателен. Наверняка ты умеешь что-то такое, чему другие очень хотят научиться. ",
           "Принимай мир таким, какой он есть. Откажись от оценочных суждений, принимай все явления как изначально нейтральные. А еще лучше – как однозначно позитивные. ",
           "Забудь о том, что было в прошлом. Оно не имеет никакого отношения к твоему будущему. Возьми с собой оттуда только опыт, знания, хорошие отношения и положительные впечатления. ",
           "Сделай отжимания в 21 повторение.",]
MESSAGES = ["""Вот доступные мне команды:

/start - начало взаимодействия с ботом  
/help - помощь (это сообщение)
/survey - минизнакомство  
/hmdil - сколько дней ты прожил(а)
/wiseness - случайная цитата  
/random_advice - совет от бота  
/usd_to_rub - конвертация значения рубля к доллару
/convert - конвертировать любую валюту в RUB
/art - моя случайная картинка
/media - my social media
/chat_id - chat id  
/secret - is only for admin

Этот бот желает Вам хорошего дня!:)""",]

CYTATES = ["""<blockquote>Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно.</blockquote>""",
           "<blockquote>Наука — это организованные знания, мудрость — это организованная жизнь.</blockquote>",
            "<blockquote>Если вы думаете, что на что-то способны, вы правы; если думаете, что у вас ничего не получится - вы тоже правы.</blockquote>",
             "<blockquote>Есть только один способ избежать критики: ничего не делайте, ничего не говорите и будьте никем.</blockquote>",
              "<blockquote>Когда я освобождаюсь от того, кто я есть, я становлюсь тем, кем я могу быть.</blockquote>",
               "<blockquote>Если нет ветра, беритесь за вёсла.</blockquote>",
                "<blockquote>Лучшее время, чтобы посадить дерево, было 20 лет назад. Следующий подходящий момент - сегодня.</blockquote>",
                 "<blockquote>Наше сознание - это все. Вы становитесь тем, о чем думаете.</blockquote>",
                  "<blockquote>Никогда не думайте, что вы уже все знаете. И как бы высоко не оценивали вас, всегда имейте мужество сказать себе: «Я невежда».</blockquote>",
                   "<blockquote>Не столь важно, как медленно ты идешь, как то, как долго ты идешь, не останавливаясь.</blockquote>",
                    "<blockquote>Если вы думаете о том, что имеете в жизни, вы всегда сможете иметь больше. Если же вы считаете, чего у вас нет, вам никогда не будет достаточно.</blockquote>",
                     "<blockquote>Мир делится на два класса — одни веруют в невероятное, другие совершают невозможное.</blockquote>",
                      "<blockquote>Мудрый человек требует всего только от себя, ничтожный же человек требует всего от других.</blockquote>",
                       "<blockquote>Всё дело в мыслях. Мысль — начало всего. И мыслями можно управлять. И поэтому главное дело совершенствования — работать над мыслями.</blockquote>",
                        "<blockquote>Думайте о прошлом, только если воспоминания приятны вам. </blockquote>",
                         "<blockquote>Если мы будем стремиться с самого начала увидеть самый конец, мы никогда не сдвинемся с места. Важно сделать первый шаг, и важно быть уверенными в том, что он правильный. </blockquote>",
                          "<blockquote>Будущее легко отнять, потому что его не существует. Это всего лишь мечтание. Трудно отнять настоящее, еще труднее – прошлое. И невозможно, доложу я вам, отнять вечность. – Он кладет ладонь мне на голову. – Если в болезни сократятся дни твои, то знай, что в таком разе вместо долготы дней тебе будет дана их глубина. Но будем молиться, чтобы и долгота не убавилась.</blockquote>",
                            ]

JOKES_URL = r"https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single"
cvt_help_message = "Укажите аргумент для конвертации, например: "

how_to_convert_usd_rub = formatting.format_text(cvt_help_message, formatting.hcode("/usd_to_rub 100"),)

cvt_how_to = formatting.format_text(cvt_help_message, formatting.hcode("/convert 100 EUR"),)

invalid_argument = "Неверный аргумент: "

error_fetching_currencies_text = "Что-то пошло не так при запросе, поробуйте снова несного позже."

error_no_such_currency = "Неизвестная валюта {currency}, укажите существующую"

set_my_currency_success_message = formatting.format_text("Валюта по умолчанию установлена:","{currency}", )

set_my_currency_help_message = formatting.format_text("Укажите выбранную валюту, например:", formatting.hcode("/set_my_currency RUB")),

set_local_currency_help_message = formatting.format_text("Необходимо указать локальную валюту, например:", formatting.hcode("/set_local_currency RUB",))

set_local_currency_success_message = "Локальная вылюта {currency} указана успешно"

set_local_currency_only_in_private_chat = ("Установка локальной валюты доступна только в личном чате")

survey_message_what_is_your_full_name = formatting.format_text("Как тебя зовут?) "
                                                               "Напиши свое полное имя.")
survey_message_full_name_is_not_text = formatting.format_text("Хмм, мне кажется это не твое настоящее имя._."
                                                              "Скажи, как тебя зовут, пожалуйста")

survey_message_full_name_ok_and_ask_for_email = formatting.format_text("У тебя красивое имя, {full_name}, я запомнил его! "
                                                                       "Напиши свой email, пожалуйста")

survey_message_email_not_okay = formatting.format_text("Не похоже на настоящий email._."
                                                       "Укажи валидный")
survey_message_email_ok = formatting.format_text("Спасибо за предоставленную информацию о вас, я не буду никак ее использовать в своих личных ботовских целях, наверное."
                                                 " У тебя хорошо дела?")
survey_message_invalid_number= formatting.format_text("Не похоже на число._.")

survey_message_invalid_yes_or_no= formatting.format_text("Не понимаю._., пожалуйста, укажите да или нет.")

survey_message_cancel = formatting.format_text("Отменилось. Заново: /survey")

your_bithday = formatting.format_text("Введи дату своего рождения, например:", formatting.hcode("/my_birthday 21.09.2004",))

media_message_text = formatting.format_text("Вот мои соцсети🌐",)
def format_message_content_currency_conversion(
   from_curr: str,
   to_curr: str,
   amount_str,
   result_amount_str,
):
   content = types.InputTextMessageContent(
      message_text = formatting.format_text(
         f"{formatting.hcode(amount_str)} {from_curr} в {to_curr}:",
         formatting.hcode(result_amount_str),
         ), 
      parse_mode= "HTML",
   )
   return content

def format_content_to_result_article(
     from_currency: str,
     to_currency: str,
     amount,
     total_amount,
):
     from_curr = from_currency.upper()
     to_curr = to_currency.upper()
     amount_str = f"{amount:,}"
     result_amount_str = f"{total_amount:,.2f}"
     content=format_message_content_currency_conversion(from_curr=from_curr,to_curr=to_curr,amount_str=amount_str,result_amount_str=result_amount_str,)
     result = types.InlineQueryResultArticle(
         id=f"{from_currency}-{to_curr}-{amount}",
         title=f"{result_amount_str}{to_curr}",
         description=f"{amount_str}{from_curr}={result_amount_str}{to_curr}",
         input_message_content=content,)
     return result


def prepare_default_result_article(query_id):
   content = types.InputTextMessageContent(
      message_text = formatting.format_text(
         formatting.hbold("Сообщение из inline запроса"),
         f"id запроса inline: {formatting.hcode(query_id)}",
      ),
      parse_mode = "HTML",
   )
   result = types.InlineQueryResultArticle(
      id = "default-answer",
      title = "Inline cooбщение",
      description = "Информация о текущем запросе и ответе",
      input_message_content = content,
   )
   return result
#good_morning = ["""Доброго утра!!!""","""С добрым утром!!""",]


def format_currency_convert_message(from_currency, to_currency, from_amount, to_amount):
   return formatting.format_text(formatting.hcode(f"{from_amount:,}"), f"{from_currency.upper()} это примерно", formatting.hcode(f"{to_amount:,.2f}"), to_currency.upper(), separator = " ", )


def format_convert_usd_to_rub(usd_amount, rub_amount):
   return format_currency_convert_message(from_currency="USD",to_currency= "RUB",from_amount= usd_amount, to_amount= rub_amount,)
  



def get_random_joke_text():
   response = requests.get(JOKES_URL)
   if response.status_code != 200:
      return "Error"
   json_data: dict = response.json()
   if json_data.gets("error"):
      return "Error"
   return json_data["joke"]