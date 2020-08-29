def testFunc(x):
    """
    @name: testFunc
    @required: testFunc2, testFunc3
    """
    return x + 1

def moreFunc(y, z):
    """
    @name: multiply
    @description: basic multiplication function
    """
    val = y * z
    return val

def noDocFunc(test):
    testString = str(test) + " this is a test"
    return testString