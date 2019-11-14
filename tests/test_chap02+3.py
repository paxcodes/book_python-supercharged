from chap02_2 import stripFirstAndLast2characters
from chap03_postfix import evaluatePostfixExpression


def test_stripFirstAndLast2characters():
    test_data = {
        "489023102": "90231",
        "hello": "l",
        "": "",
    }

    for key in test_data:
        result = stripFirstAndLast2characters(key)
        assert test_data[key] == result


def test_postfix():
    test_data = {
        "7 3 +": 10,
        "10 5 *": 50,
        "10 5 * 7 3 + /": 5.0,
        "1 2 / 3 4 / +": 1.25,
        "2 4 2 3 7 + + + *": 32,
    }

    for key in test_data:
        result = evaluatePostfixExpression(key)
        assert test_data[key] == result
