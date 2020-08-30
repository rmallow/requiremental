import parser
import libObject
import logging

class library():
    def __init__(self, parser):
        self.m_objSpecs = []
        self.m_parser = parser

    def loadFile(self, filePath, marker):
        self.m_objSpecs.extend(self.m_parser.loadFile(filePath, marker))
        
    def printObjSpecs(self):
        print(self.m_objSpecs)

    def prettyPrintObjSpecs(self, specArgList = []):
        if type(specArgList) is list and len(specArgList) > 0:
            for objSpec in self.m_objSpecs:
                for specArg in specArgList:
                    if specArg in objSpec:
                        print(str(specArg) + ": " + str(objSpec[str(specArg)]))
        else:
            for objSpec in self.m_objSpecs:
                if 'call' in objSpec:   
                    print(str(objSpec['call']))
                for key, value in objSpec.items():
                    if key != 'call':
                        print("\t" + str(key) + ": " + str(value))

    def sort(self, objs):
        newObjList = []


        return newObjList

    def lookupID(self, libObj):
        """
        find match for object in specs, return spec id
        """
        for objSpec, index in enumerate(self.m_objSpecs):
            if libObj.m_obj is objSpec['call']:
                return index

        logging.warning("obj not found in library")