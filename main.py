
from operations import Mymath
from utility_functions import is_valid, cast, add_brackets
from calculate import calculate

if __name__ == '__main__':
    lst = []
    try:
        equation = input("enter a mathematical equation: ")
    except EOFError as err:
        print(err)
    else:
        for character in equation:
            if character == ' ' or character == '\t':
                continue
            lst.append(character)
        if is_valid(lst):
            lst = cast(lst)
            if lst[0] != '(':
                lst = add_brackets(lst)
            print(lst)
            try:
                print(calculate(lst))
            except (SyntaxError, OverflowError) as e:
                print(e)
