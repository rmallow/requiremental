from requiremental.library import library
from requiremental.libGroup import libGroup
from requiremental.libObject import libObject

import test.testLibrary as testLibrary
import test.testFile2 as testFile2

def main():
    lib = library()
    lib.loadFile("test/testLibrary.py")
    lib.loadFile("test/testFile2.py")

    group = libGroup(library=lib)
    group.insert(testFile2.emaAverageAverage)
    group.insert(testLibrary.testFunc)
    group.insert(testLibrary.moreFunc)
    group.insert(testLibrary.noDocFunc)
    group.insert(testLibrary.myNameIsTestFunc2)
    testObj = libObject(testLibrary.otherFunc, details= {'name':'Close'})
    group.insert(testObj)
    group.insert(testFile2.ema)
    group.insert(testFile2.emaAverage)
    group.insert(testFile2.otherFileFunc)
    group.sort()
    group.prettyPrint()

if __name__ == '__main__':
    main()



