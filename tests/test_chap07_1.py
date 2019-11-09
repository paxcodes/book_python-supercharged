from chap07_1 import matchSentence


def test_matchSentence1():
    text = '''See the U.S.A. today. It's right here, not a world away. Average temp. is 66.5.'''

    assert matchSentence(text) == [
        'See the U.S.A. today.',
        "It's right here, not a world away.",
        'Average temp. is 66.5.'
    ]
