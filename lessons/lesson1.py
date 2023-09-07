# ОПП, алгоритмы, базы данных, GIT

# Class: методы свойства экземпляры

# lambda

# def a(b, c):
#     print(b + c)
#
# a(6, 8)


class Human:            # с большой буквы
    body = True         # свойства
    name = 'Umar'

    # магические методы
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n'

    # def __len__(self):    # дз узнать длину
    #     return f'{len(self.name)}'

    def run(self):      # методы
        print('run', self.name)


human = Human('Umar', 16)         # экземпляры
human1 = Human('Salli', 17)

print(len(human))
print(human1)

# human.run()
# human1.run()

# a = 1, 2.3, 'str', True, [], {}, ()
#
# print(type(a))