from operations import *
from utility_functions import isValid, Cast

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
        if isValid(lst):
            lst = Cast(lst)
            print(lst)
