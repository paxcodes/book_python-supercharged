import re


def matchSentence(text):
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return sentences
