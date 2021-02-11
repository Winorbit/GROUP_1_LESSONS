import requests

"""
Задача - сделать бота, который будет подсказывать нам курс валют по данным нацбанака Белки. 
Нас инеесует следующий алгоритм - ввели запрос вроде "Хочу узнать курс USD, EUR"  и в ответ получили текстовое сообщение.

Окей, это можно разбить на две части - собственно, работу с самим телеграмом, т.е отправку сообщения боту и получния ответа от него и сама программа, осуществляющая поиск, рассчети генерацию текста.

Бот просто принимает и отправляет сообщения ,следоватлеьно то униввесальная штука, так что займемся скриптом по рабтае с курсами.

Что нам нжно?
- Извлечь информацию о курсах в каком-то виде
- трансформировать в удобный нам вид
- создать из него текствое сообщение.
"""

# Итак, получается ,нам понадобяся следующие функции:

def extract_currencies():
    pass

def filter_currencies():
    pass

def create_message():
    pass

"""
И мы должны наполнить их содержанием. Наччнем с извлечения.
находится эта информация вот здесь, по ссылке - "https://www.nbrb.by/api/exrates/rates?periodicity=0"

Учитывая, что мы будем ее не раз использовать, лучше нам привзяать это значение к ссылке
"""
today_currencies_link = "https://www.nbrb.by/api/exrates/rates?periodicity=0"

# Окей, давайте сходим по этому аддресу из нашего питоновского скрипта
req = requests.get(today_currencies_link)

print(req)

"""
Так, хмм, все равно не совсем то, что нам нужно.
Вспомним, что мы посылаем ЗАПРОС и на него получаем ОТВЕТ, response
И этот респонс состоит из нескольких частей - статус, заголовки и тело.
Нас интерсует что?
Нет, не body, сначала нас интересует статус. Почему? Потому, что статус быстро говорит нам - удачен запрос или нет. И вот если удачен - тогда мы смотрим уже тело. 

После этого идем смотреть тело.
"""

req = requests.get(today_currencies_link)
if req.status_code == 200:
    print(req.json())


"""
Супер, вот это вот то, что надо!
Но! Вот только нам нужно, чтобы этот кусочек кода был переисползуемым. 
Зачит, пора запаковать это дело в функцию
"""

def extract_currencies():
    req = requests.get(today_currencies_link)
    currencies = req.json()
    return currencies

currs = extract_currencies()
print(currs)


"""
Супер, первый наш этап пройден! Мы получили большой кусок информации. Теперь наша задача его как-то отфильтровать
Как? А мы бдем искать по аббревиатуре, верно?
Соответственно, нам нужно взять те аббревиатуры, которые нас интересуют, и начать перебирать словари, из которых состои большой список. 
Затем сравнивать значение по ключу - если аббревитура входит в словарь, ты мы берем этот словарь, если нет - пропускаем.

Соответственно, нам нужно ответить на следующие вопросы
- как мы перебирем элементы?
- как мы их переберем в новую коробку?

- цикл фор, 
- класть в следующий список.

- а почему список? У нас же тупля есть, да и дикт.

Так, падажжы, а вот откуда эти аббревиатуры?
C чем же нам сравнивать
Агаа, давайте их на вход.
"""

def filter_currs(currencies:list, abbrs:list): 
    actual_data = []
    for x in currencies:
        if x["Curr"] in abbrs:
            actual_data += x
    return actual_data

# Окей, мы на вход подаем список. Но вот возникает воппрос - удобно ли это? 
# А вот теперь очень интересная штука. Давайте-ка мы вспомним про * и **


filtered_currs = filter_currencies()
print(filtered_currs)

"""
Так, супер, то есть мы извлекли данные, а затем написали функцию, которя фильтрут входящие данные по определнным парметрам.
Эту функцию фильтра мы используе для фильтрации извлеченных данных.

Теперь финальный этап - надо эту отфильтрованную информацию использовать для подстановки в шаблон и венуть сообщение, сгенерированное на основе этого шаблона.

Займемся функцией создания сообщения
"""

def create_message(currencies:list, *abrs):
    requested_currs = filter_currs(currencies, *abrs)
    message = "Курс валют в РБ на сегодня: "
    if currencies:
        for curr in requested_currs:
            abbr = curr["Cur_Abbreviation"]
            currency = round(curr["Cur_OfficialRate"],2)
            scale = curr["Cur_Scale"]
            message += f"{currency} рублей за {scale} {abbr}, "
        return message
"""
Но, парни, впомним про декомпозицию.Видите, у нас есть реквест прямо в функции. Т.е у нас идет и поход по адддресу и очистка. А нам куда правильнее будет сделать так, чтобы у нас каждая функция делала одно дело. Т.е лучше разобьем функцию создания сообщения на две - подготовку и, собственно, создание сообщения
"""

def prepare_currencies_message(requested_currs:list):
    message_template = "Курс валют в РБ на сегодня: "
    for curr in requested_currs:
        abbr = curr["Cur_Abbreviation"]
        currency = round(curr["Cur_OfficialRate"],2)
        scale = curr["Cur_Scale"]
        message_template += f"{currency} рублей за {scale} {abbr}, "
    return message_template
    pass

def request_current_courses(*requested_currs):
    current_currencies = extract_current_currencies()
    filtered_currs = filter_currs(current_currencies, *requested_currs)
    message = prepare_currencies_message(filtered_currs)
    return message
    pass

"""
Окей, парни, теперь такой момент. Вот этот код продуктовый? Вообще нет. Дело в том, что мы учитываем только хэпи-пас, и у нас есть еще не изученный варинт исключений или просто как-то учитывать возможность того, что все пойдет не так. 
Гуд, ну, тогда давате добави такие штуки, как иф-элс в случае непредвиденного ответа от сервака
"""

"ИЗМЕНЕННАЯ"
def extract_current_currencies():
    req = requests.get(today_currencies_link)
    if req.status_code == 200:
        currencies = req.json()
        if currencies:
           return currencies
        else:
            print(f"Sorry, on some reasons currencies is {currencies}")
    else:
        print(f"Request to {today_currencies_link} was failed witth status {req.status_code}")

"ОСТАЛИСЬ ПРЕЖНИМИ"

def filter_currs(currencies:list, *abrs):
    result = [curr for curr in currencies if curr["Cur_Abbreviation"] in abrs]
    return result
    pass

def prepare_currencies_message(requested_currs:list):
    message_template = "Курс валют в РБ на сегодня: "
    for curr in requested_currs:
        abbr = curr["Cur_Abbreviation"]
        currency = round(curr["Cur_OfficialRate"],2)
        scale = curr["Cur_Scale"]
        message_template += f"{currency} рублей за {scale} {abbr}, "
    return message_template
    pass

def request_current_courses(*requested_currs):
    current_currencies = extract_current_currencies()
    filtered_currs = filter_currs(current_currencies, *requested_currs)
    message = prepare_currencies_message(filtered_currs)
    return message
    pass


