import pytest
from chap10_2 import Money


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
    assert Money('3.0') != oneUsd + twoCad
