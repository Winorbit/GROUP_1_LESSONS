from courses import Courses
from weather import Weather
import requests

class Bot(Courses, Weather):
    def __init__(self, country="", weather_token="", city=""):
        self.country = country
        self.city = city
        self.weather_token = weather_token
        super(Weather, self).__init__()
        super(Courses, self).__init__()


    def city_weather_message(self, weather:dict, message_long:bool=False)->str:
        #message = 
        #if keys in 
        if not message_long:
            short_weather_info = weather["weather"]
            short_weather_message = f"Weather in {self.city} is {short_weather_info['description']}"
            return short_weather_info

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

    def send_city_weather_message(self):
        weather_data = self.get_current_weather()
        message_text = self.city_weather_message(weather=weather_data)
        #send_text
    
    def send_actual_course(self, money_abbr:str=""):
        message = self.actual_course_message(money_abbr=money_abbr)
        #send_text


#bot = Bot(bot_token="", country="uk", weather_token="274e16bcd29fc6003638a44b00f207cd", city="London")
#bot.actual_course_message(money_abbr="USD")

#- зависимость от страны


class TelegramBot(Bot):
    root_url = "https://api.telegram.org/bot" 
    get_me = "/getMe"
    updates = "/getUpdates"
    message = "/sendMessage"

    def __init__(self, bot_token=None, country="", weather_token="", city=""):
        self.token = bot_token
        self.country = country
        self.city = city
        self.weather_token = weather_token
        super().__init__(country=country, weather_token=weather_token, city=city)
        #super(Bot, self).__init__()

    def get_bot_info(self):
        try:
            url = f"{self.root_url}{self.token}{self.get_me}"
            print(url)
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



#bot = TelegramBot(bot_token="1564817798:AAHsKi8dsB9ETgnDNEGDdS-R-jdyTuOwDJo", country="rb", weather_token="", city="Minsk")
#message = bot.actual_course_message(money_abbr="USD")
#print(message)
#print(bot.get_bot_info())
