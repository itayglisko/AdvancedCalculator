from math import pow


class Mymath:
    @staticmethod
    def add(num1: float, num2: float) -> float:
        """
        calculate num1 + num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return float(num1 + num2)

    @staticmethod
    def sub(num1: float, num2: float) -> float:
        """
        calculate the subtraction between num1 and num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return float(num1 - num2)

    @staticmethod
    def mul(num1: float, num2: float) -> float:
        """
        calculate nun1 * num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return float(num1 * num2)

    @staticmethod
    def div(num1: float, num2: float) -> float:
        """
        calculate num1/num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        if num2 == 0:
            raise ArithmeticError("Can not divide by zero")
        return float(num1 / num2)

    @staticmethod
    def pow(num1: float, num2: float) -> float:
        """
        calculate num1 to the power of num2 (num1^num2)
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        :raise: ArithmeticError if the 2 parameters are 0
        """
        if num1 == 0 and num2 == 0:
            raise ArithmeticError("Math Error 0^0 is undefined")
        return pow(num1, num2)

    @staticmethod
    def avg(num1: float, num2: float) -> float:
        """
        calculate the average between num1 and num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return (num1 + num2) / 2

    @staticmethod
    def max(num1: float, num2: float) -> float:
        """
        choosing the bigger number between num1 and num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return num1 if num1 > num2 else num2

    @staticmethod
    def min(num1: float, num2: float) -> float:
        """
        choosing the lower number between num1 and num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return num1 if num1 < num2 else num2

    @staticmethod
    def reminder(num1: float, num2: float) -> float:
        """
        calculate the reminder from the operation num1/num2
        :param num1: A parameter that is involved on the operation
        :param num2: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return num1 % num2

    @staticmethod
    def tilda(num: float) -> float:
        """
        making num to be the opposite number of it
        :param num: A parameter that is involved on the operation
        :return: the result from the operation
        """
        return -num

    @staticmethod
    def factorial(num: float) -> float:
        """
        calculate the factorial of the parameter
        :param num: A parameter that is involved on the operation
        :return: the result from the operation
        :raise: ArithmeticError if the parameter is either negative or float
        """
        if not int(num) == num:
            raise ArithmeticError("Factorial is not defined for float numbers.")
        if num < 0:
            raise ArithmeticError("Factorial is not defined for negative numbers.")
        elif num == 0:
            return 1
        return Mymath.factorial(num - 1) * num

    @staticmethod
    def hashtag(num: float) -> float:
        """
        summing up all the digits of the parameter num
        :param num: A parameter that is involved on the operation
        :return: the result from the operation
        """
        sum = 0
        if num < 0:
            raise ValueError("can not calculate hashtag on a negative number")
        else:
            num = -num
        num = str(num)
        for digit in num:
            if digit.isdigit():
                sum += int(digit)
        return sum
