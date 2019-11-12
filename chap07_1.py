import re


def matchSentence(text):
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return sentences


def getSentences(text):
    """
    Sentences could have multiple spaces in-between and can start with
    a number.
    """
    pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'
    matches = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return matches
