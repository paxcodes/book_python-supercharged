import re
from chap07_2 import getSentences


def test_getSentence1_useRegex():
    text = '''See the U.S.A. today.     \tIt's right here,\n\n not a world away.\n66.5 is the average temp.'''

    expectedList = [
        'See the U.S.A. today.',
        "It's right here, not a world away.",
        '66.5 is the average temp.'
    ]

    expectedSentences = '''See the U.S.A. today. It's right here, not a world away. 66.5 is the average temp.'''
    assert getSentences(text, useRegex=True) == (
        expectedSentences, expectedList)


def test_getSentence1():
    text = '''See the U.S.A. today.     \tIt's right here,\n\n not a world away.\n66.5 is the average temp.'''

    expectedList = [
        'See the U.S.A. today.',
        "It's right here, not a world away.",
        '66.5 is the average temp.'
    ]

    expectedSentences = '''See the U.S.A. today. It's right here, not a world away. 66.5 is the average temp.'''
    assert getSentences(text) == (
        expectedSentences, expectedList)
