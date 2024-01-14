from utility_functions import validkey, regular_opt, right_unary
from operations import Mymath


def calculate(lst: list[any]) -> float:
    """
    gets a casted list and calculate the mathematical sequence
    :param lst: a list full of the use's input
    :return: the outcome of the equation
    """
    bracketslst = []
    while is_brackets(lst):
        bracketslst = equation_in_the_bracket(lst)
        while is_brackets(bracketslst):
            bracketslst = equation_in_the_bracket(bracketslst)
        opt_index = first_to_calc(bracketslst)
        if opt_index == -1:
            remove_useless_bracket(lst)
            continue
        result = calc(bracketslst, opt_index)
        where = sublist_index(lst, bracketslst)
        if regular_opt(lst[where + opt_index]):
            lst[where + opt_index] = result
            del lst[where + opt_index - 1]
            del lst[where + opt_index]
        elif right_unary(lst[where + opt_index]):
            lst[where + opt_index] = result
            del lst[where + opt_index - 1]
        else:
            lst[where + opt_index] = result
            del lst[where + opt_index + 1]
        remove_useless_bracket(lst)
        print(lst)
    return lst[0]


def remove_useless_bracket(lst: list[any]) -> list:
    """
    checks if there is useless brackets and remove it for example 9+(3) will be 9+3
    :param lst: list full of the user's input
    :return: the list without the useless brackets
    """
    idx = -1
    for index, element in enumerate(lst):
        if element == '(':
            idx = index
        elif element == ')':
            if idx + 2 == index:
                del lst[index]
                del lst[idx]
    return lst


def calc(lst: list[any], idx: int) -> float:
    """
    calculate the outcome of the operation
    :param lst: list full of the user's input
    :param idx: where the operator is
    :return: the outcome of the operation
    """
    result = -1
    match lst[idx]:
        case '+':
            result = Mymath.add(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '-':
            result = Mymath.sub(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '*':
            result = Mymath.mul(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '/':
            result = Mymath.div(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '^':
            result = Mymath.pow(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '%':
            result = Mymath.sub(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '@':
            result = Mymath.avg(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '$':
            result = Mymath.max(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '&':
            result = Mymath.min(lst[idx - 1], lst[idx + 1])
            # lst[idx - 1:idx + 2] = None
        case '~':
            result = Mymath.tilda(lst[idx + 1])
            # lst[idx:idx + 2] = None
        case '!':
            result = Mymath.factorial(lst[idx - 1])
            # lst[idx - 1:idx + 1] = None
        case '#':
            result = Mymath.hashtag(lst[idx - 1])
            # lst[idx - 1:idx + 1] = None
        case 'm':
            result = -lst[idx + 1]
    return result


def sublist_index(lst: list[any], sublst: list[any]) -> int:
    """
    gets 2 which the second 1 is a sublist of the first one and return the index of where the sublst is in the lst
    :param lst: the whole equation
    :param sublst: a list which is a sublist of lst
    :return: the starting index of where the sublst is in the lst
    """
    for index, element in enumerate(lst):
        if element == sublst[0]:
            if lst[index:index + len(sublst)] == sublst:
                return index
    return -1


def first_to_calc(lst: list[str, float]) -> int:
    """
    gives the index of the strongest operator in the equation
    :param lst: list full of the user's input
    :return: an integer type parameter which is the index
    """
    power = 0
    idx = -1
    for index, e in enumerate(lst):
        if validkey(e):
            if power < kdimut(e):
                idx = index
                power = kdimut(e)
    return idx


def kdimut(ch: str) -> float:
    """
    checks what is the priority of the operator
    :param ch: a char represents an operator
    :return: the power of the operator
    """
    match ch:
        case '+' | '-':
            return 1
        case '*' | '/':
            return 2
        case '^':
            return 3
        case 'm':
            return 3.5
        case '%':
            return 4
        case '@' | '$' | '&':
            return 5
        case '!' | '~' | '#':
            return 6
    return 0


def is_brackets(lst: list[any]) -> bool:
    """
    checks if there is a brackets in the equation
    :param lst: list full of the user's input
    :return: true if there is a brackets and false if not
    """
    for character in lst:
        if character == '(':
            return True
    return False


def equation_in_the_bracket(lst: list[str, float]) -> list[str, float]:
    newlst = []
    flag = False
    idx = -1
    count = 0
    for index, character in enumerate(lst):
        if character == '(':
            flag = True
            if idx == -1:
                idx = index
        if character == ')':
            if count > 0:
                count -= 1
            else:
                flag = False
        if flag and idx != index:
            newlst.append(character)
            if character == '(':
                count += 1
    return newlst
