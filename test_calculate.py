import pytest
from main import remove_white_spaces
from utility_functions import cast, add_brackets, is_valid
from calculate import calculate


def test_calculate():
    """
    testing several equations to check that the calculator answer every situation
    there are 3 types of test one of valid and legal equations.
    second that the function "is valid" taking care of which need to return False
    and the last one which raises exceptions.
    :return:
    """
    assert calculate(add_brackets(cast(remove_white_spaces("100@50")))) == 75
    assert calculate(add_brackets(cast(remove_white_spaces("234 -   4")))) == 230
    assert calculate(add_brackets(cast(remove_white_spaces("3^5")))) == 243
    assert calculate(add_brackets(cast(remove_white_spaces("345#&   10")))) == 10
    assert calculate(add_brackets(cast(remove_white_spaces("5!$121")))) == 121
    assert calculate(add_brackets(cast(remove_white_spaces("234+54.2")))) == 288.2
    assert calculate(add_brackets(cast(remove_white_spaces("34#*3+4!-(-7-----9)$123")))) == -78
    assert calculate(add_brackets(cast(remove_white_spaces("~12^3+~-9/6.2")))) == -1726.5483870968
    assert calculate(add_brackets(cast(remove_white_spaces("~(5*2+~(3!))")))) == -4
    assert calculate(add_brackets(cast(remove_white_spaces("(-3-(-(-3)))")))) == -6
    assert calculate(add_brackets(cast(remove_white_spaces("---(~3-(9*9^(1/2)*(-1)))")))) == -24
    assert is_valid(remove_white_spaces("")) == False
    assert is_valid(remove_white_spaces("4~@3")) == False
    assert is_valid(remove_white_spaces("10+*200")) == False
    assert is_valid(remove_white_spaces("fuiqeh434^3761890*3211")) == False
    assert calculate(add_brackets(cast(remove_white_spaces("((12 &    53) #)!")))) == 6
    assert calculate(add_brackets(cast(remove_white_spaces("4!^2+(64/8)/4*(10@5&7+2-(22#))")))) == 586
    assert calculate(add_brackets(cast(remove_white_spaces("((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) % 3)! + ~-------((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) %  3)!")))) == 2
    assert calculate(add_brackets(cast(remove_white_spaces("((-------45/-9)^2/5%2+5)/6")))) == 5
    assert calculate(add_brackets(cast(remove_white_spaces("(6!$1000/10)^0.5/2.5")))) == 4
    assert calculate(add_brackets(cast(remove_white_spaces("12.3+5.6*4-(8.1^2)")))) == -30.909999999999997
    assert calculate(add_brackets(cast(remove_white_spaces("~6.4+3.2/2*7-(5.1^1)")))) == -0.29999999999999893
    assert calculate(add_brackets(cast(remove_white_spaces("9.8/2.1+4^3-(~7.2)")))) == 75.8666666667
    assert calculate(add_brackets(cast(remove_white_spaces("2.4/1.3*~6.2^2")))) == 70.96615384792801
    assert calculate(add_brackets(cast(remove_white_spaces("10.2/2+(~3*2)-1.8")))) == -2.7
    assert calculate(add_brackets(cast(remove_white_spaces("((4*6)+15)/(3^2)-(64^0.5+(7^3)/2)+(((10*(5^2))/25^0.5)*2)")))) == -75.1666666667
    assert calculate(add_brackets(cast(remove_white_spaces("3*5!-((20*(9-4^2))/81^0.5)+2^3*7")))) == 431.5555555556
    with pytest.raises(ArithmeticError):
        print("Running test case 6\n")
        calculate(add_brackets(cast(remove_white_spaces("87.7+-456^2/56%4"))))
    with pytest.raises(ValueError):
        calculate(add_brackets(cast(remove_white_spaces("3--4#"))))
    with pytest.raises(SyntaxError):
        assert is_valid(remove_white_spaces("--~12"))
        assert is_valid(remove_white_spaces(".+45"))

