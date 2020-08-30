from library import library
from parser import parser

def main():
    parse = parser(settingsPath = "src/settings.yml")
    lib = library(parse)
    lib.loadFile("src/testLibrary.py", "@")
    lib.loadFile("src/testFile2.py", "@")
    lib.prettyPrintObjSpecs()


if __name__ == '__main__':
    main()



