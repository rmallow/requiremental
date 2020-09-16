from library import library
from parser import parser
from libGroup import libGroup
from libObject import libObject

import testLibrary
import testFile2

def main():
    parse = parser(settingsPath = "src/settings.yml")
    lib = library(parse)
    lib.loadFile("src/testLibrary.py", "@")
    lib.loadFile("src/testFile2.py", "@")
    lib.prettyPrintObjSpecs()

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



