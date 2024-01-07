import math
from math import pow


class My_math(object):
    def add(num1: float, num2: float) -> float:
        try:
            return float(num1 + num2)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")

    def sub(num1: float, num2: float) -> float:
        try:
            return float(num1 - num2)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")

    def mul(num1: float, num2: float) -> float:
        try:
            return float(num1 * num2)
        except (ValueError, TypeError) as err:
            print("this functions needs to get an integer or a float type")

    def div(num1: float, num2: float) -> float:
        try:
            return float(num1 / num2)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")
        except ArithmeticError as e:
            print(e)

    def pow(num1: float, num2: float) -> float:
        try:
            return math.pow(num1, num2)
        except (ValueError, TypeError) as err:
            print("this function needs to get an integer or a float type")
