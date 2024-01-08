import math
from math import pow


class Mymath:
    @staticmethod
    def add(num1: float, num2: float) -> float:
        return float(num1 + num2)

    @staticmethod
    def sub(num1: float, num2: float) -> float:
        return float(num1 - num2)

    @staticmethod
    def mul(num1: float, num2: float) -> float:
        return float(num1 * num2)

    @staticmethod
    def div(num1: float, num2: float) -> float:
        try:
            return float(num1 / num2)
        except ArithmeticError as e:
            print(e)

    @staticmethod
    def pow(num1: float, num2: float) -> float:
        return math.pow(num1, num2)

    @staticmethod
    def avg(num1: float, num2: float) -> float:
        return (num1 + num2) / 2

    @staticmethod
    def max(num1: float, num2: float) -> float:
        return num1 if num1 > num2 else num2
    @staticmethod
    def min(num1: float, num2: float) -> float:
        return num1 if num1<num2 else num2

    @staticmethod
    def reminder(num1: float, num2: float) -> float:
        return num1 % num2

    @staticmethod
    def tilda(num: float) -> float:
        return -num

    @staticmethod
    def factorial(num: float) -> float:
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif num == 0:
            return 1
        return Mymath.factorial(num-1) * num

