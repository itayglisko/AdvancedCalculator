#this methos is not finished
def isValid(lst: list[str]) -> bool:
    if alpha(lst):
        return False
    elif not Operator(lst):
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
    for charachter in lst:
        if charachter.isdigit():
            continue
        elif charachter == '(' or charachter == ')':
            continue
        elif not ValidKey(charachter):
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
