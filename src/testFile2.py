def ema(x):
    """
    @name: ema
    @required: testFunc
    """
    return x + 1

def emaAverage(y, z):
    """
    @name: emaAverage
    @required ema
    @description: basic ema Average function
    """
    val = y * z
    return val

def emaAverageAverage(test):
    """
    @name: emaAvgAvg
    @required emaAverage
    @description: basic ema Average Average function
    """
    testString = str(test) + " this is a test"
    return testString

def otherFileFunc():
    """

    """
    return 42