# множественное наследование
# venv
# инкапсуляция абстракция
# скрытые детали , класс
# 3 способа защиты публичный _приватный __скрытый
#  object class - super class


# множественное наследование

class Ded:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('sleep')

ded = Ded('Umar', 40)
ded.sleep()

class Papa(Ded):
    def work(self):
        print(self.name, 'working')      # Мирлан + воркинг

name = Papa('Mirlan', 17)
name.work()

class Otchim:
    def __init__(self,name):
        self.name = name

    def starwars(self):
        print(self.name,'im your papa')

name2 = Otchim('Nurlan')


class Son(Papa, Otchim):...

# MRO
son = Son('Luk', 17)
son.starwars()


# venv

# import math
# print(math.e)
#
# import math
# print(math.pi)

# import time, random, math
# import импортирует целый модуль
# from namemodul import pi
# moduls 3 встроенные собвственные и внешние