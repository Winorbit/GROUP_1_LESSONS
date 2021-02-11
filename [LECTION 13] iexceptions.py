try:
    1/0
except Exception:
    print("Zero division")

print("Hello")

try:
    1/0
except Exception as ddt:
    2+4


print("Bye!")

try:
    [][3]
except Exception as e:
    print("Zero division")
except IndexError:
    print("Index error")



# Окей, а если нам нужно ОБЯЗАТЕЛЬНО закончить действие? Файл закрыть, соединение оборвать и т.д

a = 1
b = 0
#b = 1

"""
try:
    a/b
except ZeroDivisionError as e:
    print("Huston, we got a problem")
finally:
    print("It hapens in every sityation")
"""
queue = 16

if queue > 15:
    raise Exception("Users in queue more thn we can process")

"""
ДОМАШНЕЕ ЗАДАНИЕ

Используя новые знания, давайте сделаем нашего бота не просто работоспособным, но - надежным, устойчивым.
Проанализируйте свой код для бота, найдите узкие места, думая с позиции того, как же можно сломать бота и добавьте 
в нужные места исключения или же иные способы избегать ошибок 

# ССЫЛКИ ДЛЯ ПОНИМАНИЯ

https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html  - Коротко и понятно по эксепшены и их список.  
Нужно ли их запоминать? Нет, достаточно знать, что они есть, и, в случае понимания, что на участке кода будет поблема того или иного толка, идти искать как именно называеться исключение нужного типа.

https://python-scripts.com/try-except-finally  - Про исключения - тоже доступно и неплохо

Отличный и подробный материал - https://dev-gang.ru/article/kak-luczshe-vsego-ispolzovat-try-except-v-python-osobenno-dlja-naczinausczih-9ivcu5omts/

Два отличных материала на анлийском о перехвате ошибок, причем не только про Exceptions, а и про то, как альтернативно работать с возможными сбоями в кодею
https://www.techbeamers.com/use-try-except-python/ 
https://medium.com/better-programming/a-comprehensive-guide-to-handling-exceptions-in-python-7175f0ce81f7
"""