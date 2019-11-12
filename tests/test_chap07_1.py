import re
from chap07_1 import matchSentence
from chap07_1 import getSentences


def test_matchSentence1():
    text = '''See the U.S.A. today. It's right here, not a world away. Average temp. is 66.5.'''

    assert matchSentence(text) == [
        'See the U.S.A. today.',
        "It's right here, not a world away.",
        'Average temp. is 66.5.'
    ]


def test_getSentence1():
    text = '''See the U.S.A. today.     \tIt's right here, not a world away. 66.5 is the average temp.'''

    assert getSentences(text) == [
        'See the U.S.A. today.',
        "It's right here, not a world away.",
        '66.5 is the average temp.'
    ]
