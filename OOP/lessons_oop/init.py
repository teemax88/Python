# Инициализатор объекта класса
# __init__(self)

# Финализатор класса
# __del__(self)

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def set_coords(self, x, y):
    #     self.x = x
    #     self.y = y

    def get_coords(self):
        return (self.x, self.y)


# вариант без __init__
# pt = Point()
# pt.set_coords(1, 2)
# print(pt.__dict__)    #{'x': 1, 'y': 2}


# Используем __init__
pt = Point(10, 20)
print(pt.__dict__)  #{'x': 10, 'y': 20}