from decimal import Decimal


def promptForSign():
    while True:
        sign = input("Enter sign (`1` for a positive, `0` for negative): ")
        if sign == "1" or sign == "0":
            break
        else:
            print("Invalid input.")

    return int(sign)


def promptForDigits():
    while True:
        digits = input("Enter digits of the decimal: ")
        if digits.isdigit():
            break
        else:
            print("Invalid input.")

    digits = [int(c) for c in digits]
    return tuple(digits)


def promptForIntegerExponent():
    while True:
        integer = input("Enter integer exponent: ")
        try:
            integer = int(integer)
        except ValueError:
            print("Invalid input.")
            continue
        break

    if integer > 0:
        print("Turning integer exponent to negative.")
        integer = -integer

    return integer


if '__main__' == __name__:
    sign = promptForSign()
    digits = promptForDigits()
    integerExponent = promptForIntegerExponent()

    dec = Decimal((sign, digits, integerExponent))
    print(dec)
