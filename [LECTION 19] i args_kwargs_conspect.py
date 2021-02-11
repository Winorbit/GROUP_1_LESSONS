# Поворение функций:
# Есть ли ограничение на тип и колличество аргументов?
# Если мы говорим ,что тип не ограничен, можем ли мы посылать на вход, наприме, словарь, дикт, тупль, и т.д?


# Идея функций как раз в том, что существует тело функции - набор исполняемых инструкций, значения в которых каждый раз задаются разные.
# И значения эти задаются с помощью аргументов.

# Однако каждый ли раз для получения разного резултата нам требуется вводить разные аргументы?
# Вопрос звучит, на первый взгляд глупо - если мне нужен, допустим, просчет маршрута до какой-то локации, конечно мне нужно вызывать функцию, которая бдукт принимать
# мои текущие координаты ,менющие по мере продвижения. Ведь если я ,скажем, буду посылать раз в 5 секунд новую длогту а широта не будет меняться ,навигатор меня приведет не туда ,куда нужно.



# Для регистации нового юзера неплохо было бы завести функцию, которая проводит, собственно ,регистрацию 
# берет аргументы и записывает их в хранлище.
# Например, в базу данных.  

# Для инфорации о пользователе мы предоставляем ему несколько полей - часть обязаельная, а часть - нет. 
# И они становятся арументыми, передающимися функции регистрации при вызове.

# И вот представим ,что у нас есть форма регистрации - есть возможность вбить имя ,почту ,пароль, поставить аватарку и добавить описание.

# Но описание и автарка это опционные поля, и наш пользователь легко может их не заполнить.


# def register_user(username, user_email, userpassword, userpick, user_description):
# 	# write this data to DB
# 	pass

# # И вызов буте происходть вот так:
# # если все поля заполнены

# register_user("Testuser", "testemail@.com", "custompass," "custom_pics/users/ssd_1.jpg", "My description")

# # Если заполнена часть.
# register_user("Testuser", "testemail@.com", "custompass" )


# # И вот при частичном заолнении мы получим ошибку - на вызов передано меньше аргументов ,чем в объявлении функции указанно.
# # Окей, тогда, нверное, можно забить недостающие аргументы типом None или пусытми строками.

# register_user("Testuser", "testemail@.com", "zukabazuka_yy" None, None)

# register_user("Testuser", "testemail@.com", "jonediesinthe_e№D","", "", "")


# Тогда нам нужно делать какую-то предварительную проверку? Скажем, брать входящий джсон-словарь, и проверять его на наличие ключей?

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№33

# ПРАКТИКА


# Данные мы принимаем в джсоне. Окей, это наши питонячьи типы и м умеем с ними работать


# income_new_user_data = {"username":"Miller", 
# 						"email":"spector@mail.ru", 
# 						"password":"some_simple_pass", 
# 						"description":None, 
# 						"userpick":"my_picture.png"}


# То сть, во-первых, у нас пробелема с проверкой.
# А, во вторых, хоть и нужно бы иметь минимум аргументов, в реаной жизни иногда получаются функции с боольшим колличеством аргументов,
# в которых реально можно запутаться ,как здесь.

# Дилемма УЛУЧШАТЬ КОД/АБОТАТЬ

# ТЕХНИЧЕСКИЙ ДОЛГ

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

# Тут мы приходим к вопросу -а можно ли поместить это проверку куда-то в аргументы?  Как-то вроде:

# def register_user(username, user_email, userpassword, if not userpick: userpick = "default.png"  user_description):
# 	# write this data to DB
# 	pass

# Или же, может даже как-то проще? Скажем, задать дефолтные аргументы. И пускай бы у нас бала такая схема - 
# в ОБЪЯВЛЕНИИ ФУНКЦИИ мы могли бы забить дефолтные значения пяти аргументов
# А в момент ВЫЗОВА передаввать только часть.


# Да, для этого есть в питоне подоход - использование того ,что называется ИМЕНОВАННЫМИ АРГУМЕНТАМИ

# def register_user(username, user_email, userpassword,  userpick = "default.png",  user_description=""):
# 	pass

# register_user("New_user", "myemail@mail.ru", "my_newpa$$")



# Что у нас обычно происходит в случае, когда в вызове мы задаем меньше агументов, чем заданно при объявлении?


# def register_user(username, user_email, userpassword,  userpick,  user_description"):
# 	pass

# show_args("username", "email@mail.com", "353t3wsacdsad")

# Ошибка с сообщением о том, что мы ввели меньше аргументов, чем требуется.


# Но если мы задаим дефолтные значчения, то такй проблемы у нас не будет, т.к если мы введем только часть аргументов или вообще никаких, 
# то вместо них подставятся дефолтные знаяения.
# def register_user(username="", user_email="", userpassword=1234567):
# 	print(username)
# 	print(user_email)
# 	print(userpassword)
# 	pass


# register_user()


# register_user(username="Douglas Adams")


# register_user(username="Douglas Adams", userpassword=42)


# register_user(userpassword=42, username="Douglas Adams", user_email="hitchuscker@gmail.com")


# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# ПОГУЛЯТЬ ПО ФАЙЛАМ ОРБИТА-АПИ
# course_type = models.CharField(max_length = 20, choices=COURSES_TYPE, db_index=True, default = COURSES_TYPE[0], verbose_name='course type - free or premium')


# Немного практики? СДЕЛАТЬ ФУНКЦИЮ ИЗВЛЕЧЕНИЯ КУРСОВ ТОЛЬКО ЗАДАННЫХ

# def get_courses(data, currencies_names=("USD","RUB")):
# 	print(data, currencies_names)
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№




# Окей, и теперь вопрос - а как это вообще работает-то? 
# То есть, что этот знак = такого делает, что получается прямо в объявлении функции задать значения аргументов по умолчанию?

# Для этого нужно понять, как функция ввообще соединяет значение, переднное при вызове с именем аргумента, заданного при обявлении.

# def register_user(username, user_email, userpassword, userpick, user_description):
# 	# write this data to DB
# 	pass

# register_user(username, user_email, userpassword, userpick, user_description)

# (username, user_email, userpassword, userpick, user_description)

# username, user_email, userpassword, userpick, user_description

# Вот, собственно, и что мы видим? Знакомая структура, да? Тупль.  
# Тупль неизменяем и тупль хранит в себе ссылки-переменные на какие-то значчения.


# То есть, при обявлении функции ее аргументы это изнчально переменные БЕЗ ЗНАЧЕНИЯ
# А, как вы помните, вот так корректно:
# var = 5
# задаем имя переменной и сразу же привязываем к ней значение 5


# а вот так 

# var

# Мы получим ошибку, т.к интерпретатор видит ИМЯ ПЕРЕМЕННОЙ и пытается взять ее значение, но это значение еще не было привязанно, и мы получаем ошибку.

# И, соответственно, когда мы задаем аргументы при объявлении функции, мы создаем тупль, который содержит в себе имена пременных, ЗНАЧЕНИЯ которых мы задаем при вызове.


# def register_user(username, user_email, userpassword, userpick, user_description):
# 	аргумент и именем sernam на самом деле просто нулевой элемент тупля, переменная username
# 	а при вызове эта переменная получает свое значение
# 	username = "egor"
# 	ARGUMENTS[0] = username
	
#     print(username) = print(ARGUMENTS[0]) 

# 	pass



# При ВЫЗОВЕ 
# register_user("egor", "egor@emailcom","mypass")

# происходит следующее
# в туплье (username, user_email, userpassword, userpick, user_description)

# первый элемент, usernameб привязвается к "egor"
# username = "egor"

# ввторой - к "email"
# и так далее.


# Поэтому-то такие аргументы тип и называется ПОЗИЦИОННЫМИ.


# И тепеь пора вернуться к тому ,как мы решили поблему аргументов с значением по умолччанию. 
# Если позоционные агументы подразумевают использование тупля, то, значит,  ИМЕНОВАННЫЕ аргументы это тоже применение какой-тоз накомой структуры.
# Той ,у которой информация храниться по принципу КЛЮЧ=ЗНАЧЕНИЕ.

# Да, это творчесое использование словаря.

# def register_user(username="", user_email="", userpassword=1234567):
# 	print(username)
# 	print(user_email)
# 	print(userpassword)
# 	pass


# У именованных агументов НЕ ВАЖНА позция, т.к обращене идет ПО КЛЮЧУ а не по ИНДЕКСУ
# Кроме того, ключ-значение не работает же без клчюа и без значения, соответственно, когда мы задаем дефолтное значение, 
# обращение по ключу всяко срабатывает.



# Теперь можно вспомнить старого знакомого - функцию print()

# print("Hello")
# print("Hello", 42)
# print("Hello", 42, 42.5, "Another str")

# Каждый  из этих вариантов сработает. Сроботает и вариант с сотней переданных аргументов. 
# То есть, наша функция принт каким-то обраозм может распечатаь абсолютно любое коллиечество переменных.

# Но как это можно реализовать известными нам способаи?  Через именованные агументы не вариант - в принт их нет.
# Позционные тоже отпадают - ведь мы никогда не знаем, сколько именно агументов придет, соответственно, если жестко зададим, то юзер может ести или больше,или меньше.


# Поэтому нам нужен какой-то выход.  И тут нам снова пригодятся возможности питона по работе с данными и их структурами.  Возможности эти - запаковка и распаковка.

# Что это за зверь такой? 
# А это возможность, позволяющая брать любой набор значений, и оборачивать его в список.
# Как это выглядит на примерах:

# *a, = 1,2,3,4,"Hello"
# print(a)
# print(type(a))


# a,b, *c = True, None, None, 1, 45.6, "Egor", "", "!!!", 56
# print(c)

# a,*b, c = True, None, None, 1, 45.6, "Egor", "", "!!!", 56
# print(b)

# Что здесь происходит? Как мы помним, тупль - неизменяемая структура - в нее нельзя добавлять элементы  удалять.  НО!  Можно менять их местами и менять их значение.
# При чем тут тупль, если мы говорили о списке?
# Дело в том ,что идея запаковки/распаковки в список тесно связана со свойствами тупля

# Сработает
# *a, = 1,2,3,4,"Hello"   
# Не сработает
# *a = 1,2,3,4,"Hello"

# Одна маленькая запятая, но разница ощутима. В первом случае мы говорим 
# Элемент кортежа, переменная а, становится ссылкой на все элементы следующего тупля (т.к значения пущены через запятую), 
# но так ,как это невозможно, все эти значения заоворачиваются в список. И а принимает значение СПИСКА содержащего все элементы.

# И именно звездочка перед переменной говорит интерпретатору, что в эту самую переменную мжно поковать символы, т.к она - список.


# И точно так же звездочка работает для распаковки

# test_list = [1,2,3,False, None, 55,6.7]
# print(test_list)
# print(*test_list)


# Да, и именно принцип упковки и распаковки позволяет создавать функции ,принимающие бесконечное число аргументов ,так, как * дает возможность превратить их все в один.
# Список, содердержащий их все.


# def test_args(*args):
# 	print(args)


# test_args("Hello!", 42, "BB", False, None, "bprd")


# Да, то есть, как и с именованными аргументами, мы имеем возможность применить особенности работы питона со структурам данных, и, используя звездочку,
# запаковатьь пришедши аргументы в один ,и дальше уже работать с ним как со списком.




# Больше того, мы только что увидели, что можно создать функцию, принимающую ЛЮБОЕ колличество позиционных аргументов с помощью запаковки/распаковки.

# Так вот, мы можем делать то же самое и с ИМЕНОВАННЫМИ аргументами.  Да, если любое колличество позиционных аргументов можно запковать в список,
# можно точно так же запаковать ЛЮБОЕ колличество ПАР КЛЮЧ-ЗНАЧЕНИЕ в ОДИН словарь.



# def show_arg(**dict_arg):
# 	print(dict_arg)

# show_arg(name="Papug", height=1.1, weight=0.2)










# def show_arg(**dict_arg):
# 	print(dict_arg.keys())
# 	print(dict_arg["message"])

# show_arg(name="Papug", height=1.1, weight=0.2, message="Helllo!")




# dict_one = {"age":25, "city":"Nightsity"}
# coords = {"lan":45.67, "lat":98.76}

# new_dict = {**dict_one, **coords}


# def test(arg, arg2, *args, **kwargs)



# Функции-  гибкй инструмент, их основная задача эт хранить инструкцию, которая выполняется с какими-ото указаннми параметрами - это аргументы.
# И для еще большей гибкости мы можем по-разному подавать эти аргументы.

# Скажем, давать некоторым из них значения по умолчанию, задавать т


# ДЗ???

