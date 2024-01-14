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
    elif not valid_tilda(cast(lst)):
        print("illegal use for ~ operator")
        return False
    elif not valid_right_opt(cast(lst)):
        print("right operator need to be next to another right opt or a number")
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
        case '+' | '-' | '*' | '/' | '^' | '@' | '$' | '&' | '%' | '~' | '!' | '#' | 'm':
            return True
    return False


def brackets(lst: list[str]) -> bool:
    """
    checks if there is a closed bracket for each opened bracket
    and remove empty brackets from the list
    :param lst:  full of the input from the user
    :return: true or false
    """
    openbracket = 0
    closebracket = 0
    idx = 0
    length = len(lst) - 1
    for index, character in enumerate(lst):
        if character == '(':
            if index != 0 and not regular_opt(lst[index - 1]):
                print("before ( there need to be an operator")
                return False
            openbracket += 1
            idx = index
        elif character == ')':
            if index == length - 1 and not right_unary(lst[index + 1]) and index == length - 1 and not lst[
                                                                                                           index + 1] == ')':
                print("u had to put right unary operator after ) at this position")
                return False
            if index < length and not validkey(lst[index + 1]) and not lst[index + 1] == ')':
                print("after ) u need to put an operator")
                return False
            closebracket += 1
            if idx + 1 == index:
                return False
                # del lst[idx:index + 1]
    if openbracket != closebracket:
        return False
    return True


def add_brackets(lst: list[str]) -> list:
    newlst = ['(']
    for character in lst:
        newlst.append(character)
    newlst.append(')')
    return newlst


def double_dot(lst: list[str]) -> bool:
    """
    checks if  there is a number that has more than 1 dot like: 1.4343.9
    :param lst: list full of user's input
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
        else:
            str1 = ""
            flag = False
    return True


def regular_opt(ch: str) -> bool:
    """
    gets a char and checks if it's a unary operator or not
    :param ch: a character from the lst
    :return: true or false
    """
    match ch:
        case '+' | '-' | '*' | '/' | '^' | '@' | '$' | '&' | '%':
            return True
    return False


def right_unary(ch: str) -> bool:
    """
    check if ch is a right unary symbol
    :param ch: the char we are checkeing
    :return: true or false
    """
    match ch:
        case '!' | '#':
            return True
    return False


def is_number(x: any) -> bool:
    """
    checks if the parameter x is a number or not
    :param x:
    :return:
    """
    try:
        float(x)
        return True
    except ValueError as err:
        return False


def valid_tilda(lst: list[str, float]) -> bool:
    """
    gets a !casted! list (a list which the cast function was performed)
    and check if there is a correct use for the operator tilda '~'
    :param lst: list full of the user's input
    :return: true or false
    """
    flag = False
    valid = False
    for index, character in enumerate(lst):
        match character:
            case '~':
                flag = True
                try:
                    if (index == 0 and is_number(lst[index + 1]) or regular_opt(lst[index - 1]) and
                            is_number(lst[index + 1]) or lst[index - 1] == '(' and
                            is_number(lst[index + 1])):
                        valid = True
                    else:
                        return False
                except IndexError as e:
                    break
    if not flag:
        return True
    return valid


def valid_right_opt(lst: list[str, float]) -> bool:
    """
    checks if the right unary operators r being used right
    :param lst: list full od the user's input
    :return: true or false
    """
    flag = False
    valid = False
    for index, character in enumerate(lst):
        if right_unary(character):
            flag = True
        if index == 0 and right_unary(character):
            return False
        elif right_unary(character) and is_number(lst[index - 1]) or right_unary(character) and right_unary(
                lst[index - 1]):
            valid = True
        elif right_unary(character):
            return False
    if not flag:
        return True
    return valid


def cast(lst: list[str]) -> list:
    """
     gets a list that its chars are ready to be converted to numbers after using that func is_valid
    :param lst: list full of the input's user
    :return: a list
    """
    newlst = []
    str1 = ""
    length = len(lst)
    for index, character in enumerate(lst):
        if character == '-':
            if index == 0:
                newlst.append('m')
                continue
            if validkey(lst[index - 1]) and not right_unary(lst[index - 1]) or lst[index - 1] == '(':
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
                if character == '~' or character == '(' or character == ')':
                    continue
            if character == '~' or character == '(' or character == ')':
                newlst.append(character)
    if str1 != "":
        newlst.append(float(str1))
    return newlst
