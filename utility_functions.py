# this method is not finished
def is_valid(lst: list[str]) -> bool:
    """
    check if the input is correct while using the func cast for several cases.
    :param lst: a list with the input
    :return: true or false
    """
    if alpha(lst):
        print("u cant put alphabetic symbol in a math equation")
        return False
    elif len(lst) == 0:
        print("sorry this equation is empty")
        return False
    elif not operator(lst):
        print("sorry there is an operator that is illegal")
        return False
    elif not brackets(lst):
        print("sorry u r using brackets incorrectly")
        return False
    elif not double_dot(lst):
        print("A number can not contain more than 1 dot")
        return False
    elif not valid_tilda(cast(lst)):
        print("illegal use for ~ operator")
        return False
    elif not valid_right_opt(cast(lst)):
        print("right operator need to be next to another right opt or a number")
        return False
    elif not valid_binary_opt(cast(lst)):
        print("the placement of the binary opt is incorrect")
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
    :raise: Syntax error if there is no operand between brackets
    """
    openbracket = 0
    closebracket = 0
    idx = 0
    for index, character in enumerate(lst):
        if character == '(':
            if index != 0 and not regular_opt(lst[index - 1]):
                return False
            openbracket += 1
            idx = index
        elif character == ')':
            closebracket += 1
            # checks if there is an empty brackets
            if idx + 1 == index or openbracket < closebracket:
                return False
            if index < len(lst) - 1 and lst[index + 1] == '(':
                raise SyntaxError("There is lack of an operand between the brackets")
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
    :param ch: the char we are checking
    :return: true or false
    """
    match ch:
        case '!' | '#':
            return True
    return False


def left_unary(ch: str) -> bool:
    match ch:
        case '~':
            return True
    return False


def is_number(x: any) -> bool:
    """
    checks if the parameter x is a number or not
    :param x: the parameter we check if it is a number
    :return: True if the x is a number else False
    """
    try:
        float(x)
        return True
    except ValueError:
        return False


def valid_tilda(lst: list[str, float]) -> bool:
    """
    gets a !casted! list (a list which the cast function was performed)
    and check if there is a correct usage of the operator tilda '~'
    :param lst: list full of the user's input
    :return: true or false
    """
    lastidx = len(lst) - 1
    for index, character in enumerate(lst):
        if character == '~':
            if index == lastidx:
                return False
            if index < lastidx:
                if not (index == 0 and is_number(lst[index + 1]) or index == 0 and lst[index + 1] == '(' or regular_opt(lst[index - 1]) and
                        is_number(lst[index + 1]) or lst[index - 1] == '(' and
                        is_number(lst[index + 1]) or lst[index + 1] == '(' and regular_opt(lst[index - 1])):
                    return False
    return True


def valid_binary_opt(lst: list) -> bool:
    """
    checks if the placement of the binary opt is correct
    :param lst: list full of the user's index
    :return: true ot false
    """
    lastidx = len(lst) - 1
    for index, element in enumerate(lst):
        if regular_opt(element):
            if index == 0 or index == len(lst) - 1:
                return False
            if index < lastidx:
                if not (lst[index + 1] == '(' or is_number(lst[index + 1]) or left_unary(
                        lst[index + 1])):
                    return False
            if not (is_number(lst[index - 1]) or lst[index - 1] == '(' or lst[index - 1] == ')' or right_unary(
                    lst[index - 1])):
                return False
    return True


def valid_right_opt(lst: list[str, float]) -> bool:
    """
    checks if the right unary operators r being used right
    :param lst: list full od the user's input
    :return: true or false
    """
    lastidx = len(lst) - 1
    for index, element in enumerate(lst):
        if right_unary(element):
            if index == 0:
                return False
            if index < lastidx:
                if not (regular_opt(lst[index + 1]) or right_unary(lst[index + 1]) or lst[index + 1] == ')'):
                    return False
            if not (is_number(lst[index - 1]) or right_unary(lst[index - 1]) or lst[index - 1] == ')'):
                return False
    return True


def minus_handler(lst: list[str]) -> int:
    newlst = []
    at_the_begining = False
    count = 0
    for index, char in enumerate(lst):
        if char == '-':
            if index == 0:
                at_the_begining = True
            if at_the_begining:
                count += 1
        else:
            if at_the_begining:
                return count
    return 0


def cast(lst: list[str]) -> list:
    """
     gets a list and prepare it to be ready for the func calculate while helping check if the equation is valid.
     this function is the most important one because while doing so it handles the minuses and several
     validation that must be handled. for example:
     this function delete minuses if it is 2 in a row so if the equation is: --3 it will erase the 2 minuses cause it not
     necessary but because of it the function 'valid_tilda' can not check all the cases of tilda for example:
     --~-3 this equation is !not! legal but because this func erases minuses the function 'valid_tilda' see the equation as:
     ~-3 which is legal hence this func must handle this senario.
    :param lst: list full of the input's user
    :return: a list
    :raise: SyntaxError for illegal inputs
    """
    newlst = []
    str1 = ""
    length = len(lst)
    flag = False
    num_of_minus_at_the_beggining = minus_handler(lst)
    if num_of_minus_at_the_beggining % 2 == 1:
        newlst.append('m')
    elif lst[num_of_minus_at_the_beggining] == '~' and num_of_minus_at_the_beggining != 0:
        raise SyntaxError("illegal use for ~ operator")
    for index, character in enumerate(lst):
        if index < num_of_minus_at_the_beggining:
            continue
        if character == '-':
            flag = True
            if validkey(lst[index - 1]) and not right_unary(lst[index - 1]) or lst[index - 1] == '(':
                str1 += character
        if character == '~':
            if flag:
                raise SyntaxError("illegal use for ~ operator")
        if character.isdigit() or character == '.':
            minus_at_the_beginning = False
            flag = False
            str1 += character
        else:
            if str1 == '--':
                str1 = ""
                continue
            if character == '(' and str1 == '-':
                newlst.append('m')
                str1 = ""
            if str1 != '' and str1 != '-':
                if str1 == ".":
                    raise SyntaxError("'.' can not be used as an operand")
                newlst.append(float(str1))
            if str1 != '-' or str1 == "-" and index == length - 1:
                flag = False
                str1 = ""
                newlst.append(character)
                if character == '~' or character == '(' or character == ')':
                    continue
            if character == '~' or character == '(' or character == ')':
                newlst.append(character)
    if str1 != "":
        if str1 == ".":
            raise SyntaxError("'.' can not be used as an operand")
        newlst.append(float(str1))
    return newlst
