#local includes
from . import parser
from . import libObject
from .parser import parser

#external includes
import logging
import inspect

#requiredFunc must be first
requiredIdentifiers = ['requiredFunc', 'requiredName', 'requiredCategory']

def reqSetDiscard(objToCheck, libObjDiscard):
    if 'requiredFunc' in objToCheck.m_reqs:
        objToCheck.m_reqs['requiredFunc'].discard(libObjDiscard.m_name)

    #make sure that requyiredFunc is first
    for identifier in requiredIdentifiers[1:]:
        noRequired = identifier.replace("required","").lower()
        if identifier in objToCheck.m_reqs and noRequired in libObjDiscard.m_details:
            objToCheck.m_reqs[identifier].discard(libObjDiscard.m_details[noRequired])

class library():
    def __init__(self, parse=None):
        self.m_objSpecs = {}
        if parse is None:
            #loading parser with default settings
            self.m_parser = parser()
        else:
            self.m_parser = parse

    def loadFile(self, filePath, marker = "@"):
        #add moduleDict to current spec dict
        self.m_objSpecs = {**self.m_objSpecs, **self.m_parser.loadFile(filePath, marker)}
        
    def printObjSpecs(self):
        print(self.m_objSpecs)

    def prettyPrintObjSpecs(self, specArgList = []):
        if type(specArgList) is list and len(specArgList) > 0:
            for module in self.m_objSpecs:
                print(module + ":")
                for func in self.m_objSpecs[module]:
                    print(func + ":")
                    for objSpec in self.m_objSpecs[module][func]:
                        for specArg in specArgList:
                            if specArg in objSpec:
                                print(str(specArg) + ": " + str(objSpec[str(specArg)]))
        else:
            for module in self.m_objSpecs:
                print(module + ":")
                for func in self.m_objSpecs[module]:
                    print(func + ":")
                    if 'call' in self.m_objSpecs[module][func]:   
                        print(str(self.m_objSpecs[module][func]['call']))
                    for key, value in self.m_objSpecs[module][func].items():
                        if key != 'call':
                            print("\t\t" + str(key) + ": " + str(value))


    def reqSort(self, libObjs):
        """
            sorts and filters libObjs based on requirements
            items that don't fit in, either don't have all their requirements met 
            or aren't in specs, are filtered out
        """
        #first build specific requirements
        for libObj in libObjs:
            if libObj is None or libObj.m_module is None or libObj.m_name is None or libObj.m_name == "":
                logging.warning("error finding object during sort")
                logging.warning("obj: " + str(libObj.m_obj))
            else:
                if libObj.m_module in self.m_objSpecs and libObj.m_name in self.m_objSpecs[libObj.m_module]:
                    objSpec = self.m_objSpecs[libObj.m_module][libObj.m_name]
                    for identifier in requiredIdentifiers:
                        if identifier in objSpec:
                            if identifier not in libObj.m_reqs:
                                libObj.m_reqs[identifier] = set()
                            req = objSpec[identifier]
                            if isinstance(req, list):
                                libObj.m_reqs[identifier].update(req)
                            elif isinstance(req, str):
                                libObj.m_reqs[identifier].add(req)
                                

        newLibObjList = []
        #using the specificly built object requirements, build the sorted and filtered list
        change = True
        while change:
            change = False
            for libObj in libObjs[:]:   #if this loop ends with never going inside the if then it will break
                if all(not reqSet for reqSet in libObj.m_reqs.values()):  #check if requirement set is empty
                    change = True
                    newLibObjList.append(libObj)
                    for obj in libObjs:
                        #remove that item from all requirement sets
                        reqSetDiscard(obj, libObj)
                    libObjs.remove(libObj)
                    break  #break here to favor that libObjs were put in, earlier items will always be added if reqs met before later items
 

        return newLibObjList