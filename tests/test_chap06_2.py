from chap06_2 import isAPhoneNumber


def test_isAPhoneNumber():
    testData = {
        "1778 877 0897": "1 (778) 877-0897",
        "1728812": "172-8812",
        "1(888) 8979-213": "1 (888) 897-9213",
        "1 (888.8979-213": "1 (888) 897-9213",
        "(888).8979.213": "1 (888) 897-9213",
        "1 (888).8979.213": "1 (888) 897-9213",
        "728812": False,
        "1 1728812": False,
        "(88) 8979-213": False,
    }

    for key in testData:
        assert isAPhoneNumber(key) == testData[key]
