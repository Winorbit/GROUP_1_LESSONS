from courses import Courses
import requests
from settings import bot_token

class Bot(Courses):
    def __init__(self, country=""):
        self.country = country
        #super().__init__(country=country)
        super(Courses, self).__init__()

    def actual_course_message(self, money_abbr:str="")->str:
        today_currency_info = self.today_currency_by_abbr(money_abbr=money_abbr)
        if self.country == "uk":
            country_money = "грвн."
            rate = today_currency_info["rate"]
            scale = 1

        if self.country == "rb":
            country_money = "бел.руб"
            rate = today_currency_info["Cur_OfficialRate"]
            scale = today_currency_info["Cur_Scale"]

        message = f"Cегодня {scale} {money_abbr} стоит {rate} {country_money}"
        return message


"""
bot = Bot(bot_token="", country="rb")
message = bot.actual_course_message(money_abbr="USD")
print(message)
"""


class TelegramBot(Bot):
    root_url = "https://api.telegram.org/bot" 
    get_me = "/getMe"
    updates = "/getUpdates"
    message = "/sendMessage"

    def __init__(self, bot_token=None, country=" "):
        self.token = bot_token
        self.country=country
        super().__init__(country=country)
        #super(Courses, self).__init__()

    def get_bot_info(self):
        try:
            url = f"{self.root_url}{self.token}{self.get_me}"
            res = requests.get(url)
            if res.status_code in (200,201):
                return res.json()
        except Exception:
            raise Exception("connection lost")

    def get_updates(self):
        try:
            url = f"{self.root_url}{self.token}{self.updates}"
            res = requests.get(url)
            if res.status_code in (200,201):
                return res.json()
            else:
                print(res.status_code, url)
        except Exception:
            raise Exception("connection lost")

    def send_message(self, chat_id=None, text_message=None):
        if not chat_id:
            chat_id = self.get_updates()["result"][-1]["message"]["chat"]["id"]  
        
        url = f"{self.root_url}{self.token}{self.message}"
        res = requests.post(url, data={"chat_id":chat_id, "text":text_message} )
        if res.status_code in (200,201):
            return res.json()

"""
bot = TelegramBot(bot_token=bot_token, country="rb")
message = bot.actual_course_message(money_abbr="USD")
print(message)
print(bot.send_message(text_message=message))
"""
"""
bot = TelegramBot(bot_token=bot_token, country="rb")
last_message_number = 0
while True:
    updates = bot.get_updates()
    message_id = updates["result"][-1]["message"]["message_id"]
    message_text = updates["result"][-1]["message"]["text"]

    if message_id > last_message_number:
        if "/курс" in message_text:
            money_abbr = message_text[-3:]
            actual_currency_message = bot.actual_course_message(money_abbr=money_abbr)
            print(money_abbr)
            bot.send_message(text_message=actual_currency_message)
        last_message_number = message_id

"""


