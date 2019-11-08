from chap06_3 import removeExtraneousSpace


def test_removeExtraneousSpace():
    testData = {
        "Bananas      and Pajamas": "Bananas and Pajamas",
        "Mmm\twhat you say    oooh that you": "Mmm what you say oooh that you"
    }

    for key in testData:
        assert removeExtraneousSpace(key) == testData[key]
