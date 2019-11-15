import pytest

from chap09_1 import Point


@pytest.fixture
def point():
    return Point(x=1, y=2, z=3)


def test_add(point):
    testData = {
        (1, 2, 3): (2, 4, 6),
        (1, 1, 1): (2, 3, 4)
    }

    for key in testData:
        input = Point(key[0], key[1], key[2])
        expectedOutput = Point(
            testData[key][0], testData[key][1], testData[key][2])
        assert point + input == expectedOutput


def test_sub(point):
    testData = {
        (1, 2, 3): (0, 0, 0),
        (1, 1, 1): (0, 1, 2)
    }

    for key in testData:
        input = Point(key[0], key[1], key[2])
        expectedOutput = Point(
            testData[key][0], testData[key][1], testData[key][2])
        assert point - input == expectedOutput


def test_mul(point):
    testData = {
        (1, 2, 3): (1, 4, 9),
        (1, 1, 1): (1, 2, 3)
    }

    for key in testData:
        input = Point(key[0], key[1], key[2])
        expectedOutput = Point(
            testData[key][0], testData[key][1], testData[key][2])
        assert point * input == expectedOutput


def test_rmult(point):
    testData = {
        (1, 2, 3): (1, 4, 9),
        (1, 1, 1): (1, 2, 3)
    }

    for key in testData:
        input = Point(key[0], key[1], key[2])
        expectedOutput = Point(
            testData[key][0], testData[key][1], testData[key][2])
        assert input * point == expectedOutput


def test_strings(point):
    assert '(1, 2, 3)' == str(point)
    assert 'Point(x=1, y=2, z=3)' == repr(point)
