import re

spaceRegEx = re.compile(r'\s+')


def removeExtraneousSpace(text):
    text = re.sub(spaceRegEx, ' ', text)
    return text
