import pytest
from chap10_2 import Money
from chap10_2 import UnsupportedExchangeRate


@pytest.fixture
def oneUsd():
    m1 = Money('1.0')
    return m1


def test_addingMoneyWithMoneyObject(oneUsd):
    twoUsd = Money('2.0')
    assert Money('3.0') == oneUsd + twoUsd


def test_addingMoneyWithStaticValue(oneUsd):
    assert Money('3.0') == oneUsd + 2


def test_addingMoneyOfDifferentUnits(oneUsd):
    twoCad = Money('2.0', 'CAD')
    assert Money('2.5', 'CAD') == oneUsd + twoCad


def test_unknownUnitsShouldRaiseUnsupportedExchangeRateError(oneUsd):
    twoPhp = Money('2.0', 'PHP')
    with pytest.raises(UnsupportedExchangeRate):
        twoPhp + oneUsd


