class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def update_person(self):
        return self.name

    @update_person.setter
    def update_person(self, value):
        self.name = value

    def sum(self):
        return self.age + 47


a = Person("Tom", 23)
a.update_person = "Kate"
print(a.name)
print(a.sum())
