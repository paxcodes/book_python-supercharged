from decimal import Decimal


class Money(Decimal):

    def __new__(cls, v, units="USD"):
        return super(Money, cls).__new__(cls, v)

    def __init__(self, v, units="USD"):
        self.units = units

    def __str__(self):
        return super().__str__() + ' ' + {self.units}

    