# this method is not finished
def isValid(lst: list[str]) -> bool:
    if alpha(lst):
        return False
    elif not Operator(lst):
        return False
    elif not brackets(lst):
        return False
    return True


def alpha(lst: list[str]) -> bool:
    """
    a function which checks if there is a letter in the list
    :param lst: full of the input from the user:
    :return true or false:
    """
    for character in lst:
        if character.isalpha():
            return True
    return False


def Operator(lst: list[str]) -> bool:
    """
    a function that checks if all the operators in the list r legal
    :param lst: a list full of the input from the user
    :return: true or false
    """
    for character in lst:
        if character.isdigit():
            continue
        elif character == '(' or character == ')' or character == '.':
            continue
        elif not validkey(character):
            return False
    return True


def validkey(ch: str) -> bool:
    """
    checks if the ch is a valid operator
    :param ch: - a char from the input
    :return: true or false
    """
    match ch:
        case '+' | '-' | '*' | '/' | '^' | '@' | '$' | '&' | '%' | '~' | '!':
            return True
    return False

def brackets(lst: list[str]) -> bool:
    """
    checks if there is a closedbracket for each opened bracket
    and remove empty brackets from the list
    :param lst:  full of the input from the user
    :return: true or false
    """
    openbracket = 0
    closebracket = 0
    for index, character in enumerate(lst):
        if character == '(':
            openbracket += 1
            idx = index
        elif character == ')':
            closebracket += 1
            if idx + 1 == index:
                del lst[idx:index+1]
    if openbracket != closebracket:
        return False
    return True

def Cast(lst: list[str]) -> list:
    """
    gets with a correct input and convert the numbers into float
    :param lst: list full of the input's user
    :return: a list
    """
