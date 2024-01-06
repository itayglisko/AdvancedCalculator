import math
from math import pow


class My_math(object):
    def __init__(self, num: int):
        self.num = num

    def __add__(self: 'My_math', other: 'My_math') -> float:
        try:
            return float(self.num + other.num)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")

    def __sub__(self: 'My_math', other: 'My_math') -> float:
        try:
            return float(self.num - other.num)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")

    def __mul__(self: 'My_math', other: 'My_math') -> float:
        try:
            return float(self.num * other.num)
        except (ValueError, TypeError) as err:
            print("this functions needs to get an integer or a float type")

    def __truediv__(self: 'My_math', other: 'My_math') -> float:
        try:
            return float(self.num / other.num)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")
        except ArithmeticError as e:
            print(e)

    def __pow__(self: 'My_math', other: 'My_math') -> float:
        try:
            return math.pow(self.num, other.num)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")
