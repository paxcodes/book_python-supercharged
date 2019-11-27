from decimal import Decimal


class Money(Decimal):
    kRates = {
        "USDCAD": Decimal("1.33"),
        "CADUSD": Decimal("0.75")
    }

    def __new__(cls, v, units="USD"):
        return super(Money, cls).__new__(cls, v)

    def __init__(self, v, units="USD"):
        self.units = units

    def __str__(self):
        return super().__str__() + ' ' + {self.units}

    def __add__(self, other):
        if not isinstance(other, Money) or self.units == other.units:
            sum = super().__add__(other)
        else:
            try:
                rate = self.kRates[other.units + self.units]
            except KeyError:
                raise UnsupportedExchangeRate(
                    f"Exhchange rate, {other.units} to {self.units}, is not supported.")
            amount = rate * other
            sum = super().__add__(amount)

        return sum


class UnsupportedExchangeRate(Exception):
    pass
