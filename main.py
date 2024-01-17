from utility_functions import is_valid, cast, add_brackets
from calculate import calculate


def remove_white_spaces(equation: str) -> list:
    """
    checks if there are white spaces and if so then it does not append them to the list,
    this function creates a list full of the user's input while ignoring the white spaces
    :param equation: the user's input
    :return: a list without the white spaces
    """
    lst = []
    for character in equation:
        if character == ' ' or character == '\t':
            continue
        lst.append(character)
    return lst


def main():
    lst = []
    try:
        equation = input("enter a mathematical equation: ")
    except (EOFError, KeyboardInterrupt) as err:
        print(err)
    else:
        lst = remove_white_spaces(equation)
        try:
            if is_valid(lst):
                lst = cast(lst)
                lst = add_brackets(lst)
                print(lst)
                try:
                    print(calculate(lst))
                except (SyntaxError, OverflowError, KeyboardInterrupt, RecursionError, ValueError, ArithmeticError) as e:
                    print(e)
        except SyntaxError as e:
            print(e)


if __name__ == '__main__':
    main()
