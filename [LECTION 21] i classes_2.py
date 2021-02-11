class Human():
    group = "mamal"  # АТРИБУТ КЛАССА - т.е приндлежит именно классу, при создании объектов не пересоздаеться.
                     # т.е каждый объект имеет ссылку на одно и то же значение в памяти. 

    def __init__(self, xxx, height, eye_color):
        """ функция, которая позволяет задавать нам аргументы для объека, задавая ему атрибуты """
        self.name = xxx
        self.height = height
        self.eye_color = eye_color

    def say_self_name(self):
        print(f"Hello, my name is {self.name}")

    def say_hello(self, guest_name=None):
        print(f"Hello {guest_name}, my name is {self.name}")

import requests

class CoursesInfo(object):
    url = "https://www.nbrb.by/api/exrates/rates/usd?parammode=2"
    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code in (200, 201) and response.json():
            return response.json()
        else:
            print("Пожалуйста, проверьте код валюты. Возможны проблемы с доступом к серверу")  

    def get_bel_bank_currency_rate_by_date(self, response_body):
        rate = response_body["Cur_OfficialRate"]
        date = response_body["Date"]
        return rate
 
    def show_course(self):
        res = requests.get(self.url)
        return res.json()["Cur_OfficialRate"]

# courses_info = CoursesInfo().show_course()

class MyBot(CoursesInfo):
    root_url = "https://api.telegram.org/bot" 
    get_me = "/getMe"
    updates = "/getUpdates"
    message = "/sendMessage"

    def __init__(self, bot_token):
        self.token = bot_token

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

    def send_actual_course(self):
        courses_info = self.show_course()
        self.send_message(text_message = courses_info)





bot = MyBot("1564817798:AAHsKi8dsB9ETgnDNEGDdS-R-jdyTuOwDJo")
print(bot.url)

"""
MyBot("1564817798:AAHsKi8dsB9ETgnDNEGDdS-R-jdyTuOwDJo").get_bot_inf(MyBot("1564817798:AAHsKi8dsB9ETgnDNEGDdS-R-jdyTuOwDJo"))
"""

# print(bot.get_updates())
# bot.send_message(text_message = "Hello!")

# bot.send_actual_course()















































"""
ДЗ
Написали?
Если нет, быстро накидаем.
А если  у нас сущности разнесены по разным классам? Скажем, класс, берущий курсы?
Ага, есть наследование

Как это работает?

Окей, а перегрузка функций?

А как тогда, при перегрузке, сработает инит?

Дыа, именно так, сломаеься. Окей, тогда...функция СУПЕР

Ок, супер, немного про 

Class(object) и lasss()
про разницу 2.7 b 3 - это не просто штуки поменяли, но классы. Важыные

__init__
а есть еще встроенные функции

__getattr__
__setattr__


2.7
3.0


о разнице
ляябды
итераторы и генераторы

МЕТОД КЛАССА
МЕТОД ОБЪЕКТА
next
iter
перегрузка

статикметод
наследование
метаклассы

"""
