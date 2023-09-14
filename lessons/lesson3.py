class A:...   # родительский ксупер класс


class B:...   # дочерний класс
    # super

# инкапсуляция  абстракция
# git.clone
# наследование  полиморфизм


# инкапсуляция
class Bank:
    def __init__(self, name, age, key, money):
        self.name = name
        self.age = age
        self.__key = key
        self._money = money              # _ меняем сумму
    def tprint(self):
        print(self.name, self._money)    # _ меняем сумму

    def keys2(self):
        self.__keys()

    def __keys(self):
        print(self.__key)

# 1 публичный    2 приватный (_) 3 скрытный __

umar = Bank('Umar', 16, '1234umar', 1_000)
umar.tprint()
umar._money = 1_000_000      # с _ меняет сумму без _ не меняет
umar.tprint()

mirlan = Bank('Mirlan', 17, '1234mirlan', 1_000)
umar.__key = '1234mirlan'       # смена ключа
# print(umar.__key)
umar.keys2()

print(B.mro())    #  <class 'object'>]     абстракция