# this method is not finished
def is_valid(lst: list[str]) -> bool:
    """
    check if the input is correct
    :param lst: a list with the input
    :return: true or false
    """
    if alpha(lst):
        print("u cant put alphabetic symbol in a math equation")
        return False
    elif not operator(lst):
        print("sorry there is an operator that is illegal")
        return False
    elif not brackets(lst):
        print("sorry u r using brackets incorrectly")
        return False
    elif not double_dot(lst):
        print("A number can not contain two dots")
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


def operator(lst: list[str]) -> bool:
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
    idx = 0
    for index, character in enumerate(lst):
        if character == '(':
            openbracket += 1
            idx = index
        elif character == ')':
            closebracket += 1
            if idx + 1 == index:
                del lst[idx:index + 1]
    if openbracket != closebracket:
        return False
    return True


def double_dot(lst: list[str]) -> bool:
    """
    checks if  there is a number that has more than 1 dot like: 1.4343.9
    :param lst - list full of user's input:
    :return true or false:
    """
    str1 = ""
    flag = False
    for character in lst:
        if character.isdigit() or character == '.':
            str1 += character
            if character == '.' and not flag:
                flag = True
            elif flag and not character.isdigit():
                return False
    return True


def cast(lst: list[str]) -> list:
    """
     gets a list that its chars are ready to be converted to numbers after using that func is_valid
    :param lst: list full of the input's user
    :return: a list
    """
    newlst = []
    str1 = ""
    for index, character in enumerate(lst):
        if character == '-':
            if index == 0 or validkey(lst[index - 1]) and lst[index - 1] != '!':
                str1 += character
        if character.isdigit() or character == '.':
            str1 += character
        else:
            if str1 == '--':
                str1 = ""
                continue
            if str1 != '' and str1 != '-':
                newlst.append(float(str1))
            if str1 != '-':
                str1 = ""
                newlst.append(character)
    if str1 != "":
        newlst.append(float(str1))
    return newlst
