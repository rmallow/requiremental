def testFunc(x):
    """
    @required: testFunc2, testFunc3, otherFileFunc
    """
    return x + 1

def moreFunc(y, z):
    """
    @description: basic multiplication function
    """
    val = y * z
    return val

def noDocFunc(test):
    testString = str(test) + " this is a test"
    return testString

def myNameIsTestFunc2():
    """
    @required: multiply
    """
    x = 2


def otherFunc():
    """
    @description: i do literally nothing like the rest
    """
    return "yo"