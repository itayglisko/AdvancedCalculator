def isValid(lst: list[str]) -> bool:
    if alpha(lst):
        return False


def alpha(lst: list[str]) -> bool:
    """
    a function which checks if there is a letter in the list
    :param lst: full of the input from the user:
    :return true or false:
    """
    for character in lst:
        if character.isalpha():
            return False
    return True



def Operator(lst: list[str]) -> bool:
    """
    a function that checks if there is illegal operator in list
    :param lst: a list full of the input from the user
    :return: true or false
    """
    for charachter in lst:
        if not ValidKey(charachter):
            return False
    return True


def ValidKey(ch: str) -> bool:
    """
    checks if the ch is a valid operator
    :param ch: - a char from the input
    :return: true or false
    """
    match ch:
        case '+' | '-' | '*' | '/' | '^' | '@' | '$' | '&' | '%' | '~' | '!':
            return True
    return False
