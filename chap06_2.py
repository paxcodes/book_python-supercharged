import re


def isAPhoneNumber(number):
    sepRegEx = re.compile(r'[() .-]')
    number = re.sub(sepRegEx, '', number)
    regEx = re.compile(r'^(1?\d{3})?(\d{3})(\d{4})$')
    matches = regEx.match(number)

    if matches == None:
        return False
    else:
        return formatPhoneNumber(matches)


def formatPhoneNumber(matches):
    phone = ""
    optionalAreaCode = matches.group(1)
    if optionalAreaCode:
        regEx = re.compile(r'(1)?(\d{3})')
        areaCodeMatch = regEx.match(optionalAreaCode)
        phone = f'1 ({areaCodeMatch.group(2)}) '
    phone = phone + f'{matches.group(2)}-{matches.group(3)}'
    return phone
