# W Python mozesz generowac podpowiedzi, ktore sugeruja jakiego typu nalezy uzyc

# To pozwala na statyczne sprawdzanie typow jeszcze zanim uruchomimy nasz kod

# Sa to tylko podpowiedzi, dlatego tak czy inaczej mozna uruchomic aplikacje, nawet jezeli
# podane argumenty nie sa zgodne z sugerowanymi typami

# Ten sposob sugerowanie typow jest tez dobrym sposobem dokumentowania kodu

from typing import Literal, Union, Final, TypedDict, Protocol

# ------------------------------------------------------------------------------------
# Podpowiedzi dla typow podstawowych
# ------------------------------------------------------------------------------------


def rectangle_area(side_a: float, side_b: float) -> float:
    return side_a * side_b


print(rectangle_area(10, 30))
print(rectangle_area(10.2, 30.1))
# print(rectangle_area('side_a', 'side_b'))

# ------------------------------------------------------------------------------------
# Literal
# ------------------------------------------------------------------------------------


def choose_direction(direction: Literal['right', 'up', 'left', 'down']) -> None:
    if 'right' == direction:
        print('right!')
    elif 'up' == direction:
        print('up!')
    elif 'left' == direction:
        print('left!')
    elif 'down' == direction:
        print('down!')
    else:
        raise ValueError('wrong direction!')


# choose_direction('south')
choose_direction('up')


# ------------------------------------------------------------------------------------
# Union
# ------------------------------------------------------------------------------------


def add_positive(number1: int, number2: int) -> Union[int, str]:
    if number1 <= 0 or number2 <= 0:
        return 'numbers should have positive values!'
    # return float(number1 + number1)
    return number1 + number2


print(add_positive(10, 32))
print(add_positive(-1, 2))


# ------------------------------------------------------------------------------------
# Final
# ------------------------------------------------------------------------------------


MIN_VALUE: Final = 10
# MIN_VALUE = 11
print(MIN_VALUE)


# ------------------------------------------------------------------------------------
# TypedDict
# ------------------------------------------------------------------------------------


class Info(TypedDict):
    author: str
    version: float


info1 = Info(author='KM', version=1.0)
info2 = Info(author='KM', version='new')
print(info1)
print(info2)


# ------------------------------------------------------------------------------------
# Protocol
# ------------------------------------------------------------------------------------
# Pozwala sprawdzac obiekty wedlug zasady DUCK TYPING

class HasName(Protocol):
    name: str


def show_name(named_obj: HasName) -> None:
    print(f'Name of object is {named_obj.name}')


class TypeWithoutName:
    ...


class TypeWithName:
    def __init__(self, name):
        self.name = name


# twn1 = TypeWithoutName()
# show_name(twn1)
twn2 = TypeWithName('JOHN')
show_name(twn2)




