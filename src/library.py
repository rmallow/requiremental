import parser
import libObject
import logging
import inspect        

class library():
    def __init__(self, parser):
        self.m_objSpecs = {}
        self.m_parser = parser

    def loadFile(self, filePath, marker):
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
                    if 'required' in objSpec:
                        libObj.m_reqs.update(objSpec['required'])

        newLibObjList = []
        #using the specificly built object requirements, build the sorted and filtered list
        change = True
        while change:
            change = False
            for libObj in libObjs[:]:
                if not libObj.m_reqs:   #check if requirement set is empty
                    change = True
                    newLibObjList.append(libObj)
                    for obj in libObjs:
                        #remove that item from all requirement sets
                        obj.m_reqs.discard(libObj.m_name)
                    libObjs.remove(libObj)
 

        return newLibObjList