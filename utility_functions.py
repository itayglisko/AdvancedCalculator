def isValid(lst: list[str]) -> bool:
    if alpha(lst):
        return False


def alpha(lst: list[str]) -> bool:
    """
    a function which checks if there is a letter in the list
    :param lst:  full of the input from the user:
    :return true or false:
    """
    for character in lst:
        if character.isalpha():
            return False
        return True


