# аннотация выделит если значение будет не того типа что указан (переменная: тип) -> тип вывода
from typing import List, Dict, Tuple, Optional, Any, Union


# импорт подсказок после аннотации какие методы могут использоваться
# Any - любой тип, Optional - или указанное значение или None, Union объединяет несколько возможных типов
# в Python 3.10 и выше Union[int, float, str] заменена на int | float | str

def add_numbers(a: int, b: int = 130) -> int:  # если b будет указан он заменится, если нет то будет равен 130
    return a + b


def list_upper(lst: List[str]):  # lst: List[str] после импорта мы можем указать какого типа у нас будут знач-я в списке
    for elem in lst:
        print(elem.upper())


a = 100
b: int = 100  # аннотация переменной , т.е если мы в неё запишем как в следующей строке не int она запишет,
# но выведет предупреждение о том что запись не того типа
c: int = 'asd'  # есть предупреждение о том что запись не того типа
print(c)  # asd вывод
print(add_numbers(a, b))  # 200
print(add_numbers(a))  # 230 поскольку мы передали только один аргумент, а по умолчанию в функции был b = 130
print(add_numbers('hello ', 'world'))  # hello world но вывод с предупреждением что значения не того типа
print(add_numbers([1, 2, 3], [5, 6]))  # [1, 2, 3, 5, 6] но вывод с предупреждением что значения не того типа
print(add_numbers.__annotations__)  # вывод {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

print(list_upper(['as', 'qw', 'df', 'ty', 'er']))  # AS QW DF TY ER вывод
print(list_upper.__annotations__)  # {'lst': typing.List[str]}

d: dict[str, int] = {'a': 100, 'b': 200}  # при нажатии Alt+Enter Python сам подставит аннотацию

f: Any = 123  # Any означает что в переменной может храниться любой тип
f = 'asdf'
print(f)  # asdf

g: Optional[List] = [1, 2, 3]  # g не будет подчёркивать если переменная будет или списком или None
g = None
g = 123
print(g)  # 123 вывод , но 123 выше подчеркнёт поскольку Optional аннотировал её или списком или None

w: str | int | float = 123
w = 12.34
w = 'asd'
w = [1, 2, 4]
print(w)  # [1, 2, 4] вывод , но [1, 2, 4] выше подчеркнёт поскольку аннотировал её str, int или float
