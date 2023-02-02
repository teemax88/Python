class Person:
    name = 'Ivan'
    age = 30


# смотрим все атрибуты у класса
print(Person.__dict__)

# получаем атрибут класса
print(getattr(Person, 'name'))

# 3-м значением будет вывод, если мы хотим получить несуществующий атрибут
print(getattr(Person, 'x', 'Нет такого атрибута'))

# Изменяем значение атрибута
Person.name = 'Misha'
print(Person.name)

# если пытаться изменить несуществующий атрибут, то Python автоматически его создаст
Person.x = 100
print(Person.__dict__)
print(Person.x)

# Устанавливаем атрибут
setattr(Person, 'x', 200)
print(Person.x)

# Создаем новый атрибут
setattr(Person, 'y', [1, 2, 3])
print(Person.y)

# Удаляем атрбут (нельзя удалять несуществующий атрибут)
del Person.x
print(Person.__dict__)

delattr(Person, 'y')
print(Person.__dict__)

human = Person()

print(human.age)
print(human.name)

print("*******-------*******")


class Car:
    model = 'BMW'
    engine = 1.6

    # def drive():
    #     print('Hello')

    # self - подставляет тот экземпляр класса, для которого он был вызван (содержит ссылку на экземпляр класса)
    # def drive(self):
    #     print('Hello' + str(self))

    def drive(self, x, y):
        self.x = x
        self.y = y

    def getdrive(self):
        return (self.x, self.y)


a = Car()

a.drive(1, 2)
print(a.__dict__)
print(a.getdrive())

print("*******-------*******")

b = Car()
b.drive(10, 20)
print(b.__dict__)

print(a.model)
print(b.engine)

print(a.__dict__)
print(b.__dict__)

a.seat = 4
print(a.seat)

# <bound method Car.drive of <__main__.Car object at 0x00000267C6C88880>>
# a.drive

# Hello<ООП.les_1.Car object at 0x0000028B7941A080>
# a.drive()

# Hello<ООП.les_1.Car object at 0x0000028B7941A140>
# b.drive()


# <function Car.drive at 0x00000267C6BFBAC0>
# Car.drive


# Car.drive()
# getattr(Car, 'drive')()
