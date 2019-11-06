import re


def isAPhoneNumber(number):
    sepRegEx = re.compile(r'[() .-]')
    number = re.sub(sepRegEx, '', number)
    regEx = re.compile(r'^(\d{3})?(\d{3})(\d{4})$')
    matches = regEx.match(number)

    if matches == None:
        return False
    else:
        return formatPhoneNumber(matches)


def formatPhoneNumber(matches):
    phone = ""
    if matches.group(1):
        phone = f'({matches.group(1)}) '
    phone = phone + f'{matches.group(2)}-{matches.group(3)}'
    return phone
