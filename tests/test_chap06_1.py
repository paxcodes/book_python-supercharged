from chap06_1 import isAPhoneNumber


def test_isAPhoneNumber():
    testData = {
        "778 877 0897": "(778) 877-0897",
        "1728812": "172-8812",
        "(888) 8979-213": "(888) 897-9213",
        "(888.8979-213": "(888) 897-9213",
        "(888).8979.213": "(888) 897-9213",
        "728812": False,
        "(88) 8979-213": False,
    }

    for key in testData:
        assert isAPhoneNumber(key) == testData[key]
