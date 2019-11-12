import re


def getSentences(text, useRegex=False):
    """
    Replace newlines and multiple spaces with a single space.
    Then, extract sentences. A sentence can start with a number.
    """
    text = __replaceWhitespace(text, useRegex)
    pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'
    matches = re.findall(pattern, text)
    return text, matches


def __replaceWhitespace(text, useRegex):
    if useRegex:
        newLine = re.compile(r'\n+')
        text = re.sub(newLine, ' ', text)
        multiWhitespace = re.compile(r'\s+')
        text = re.sub(multiWhitespace, ' ', text)
    else:
        text = ' '.join(text.split())

    return text
