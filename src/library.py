import parser
import libObject
import logging
import inspect

def removeFromReqs(objReqs, name):
    for objReq in objReqs:
        objReq[0].discard(name)

class library():
    def __init__(self, parser):
        self.m_objSpecs = {}
        self.m_parser = parser
        self.m_reqChecked = False

    def loadFile(self, filePath, marker):
        self.m_objSpecs == {**self.m_objSpecs, **self.m_parser.loadFile(filePath, marker)}
        
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

    def fillReqIds(self):
        pass


    def reqSort(self, libObjs):
        """
            sorts and filters libObjs based on requirements
            items that don't fit in, either don't have all their requirements met 
            or aren't in specs, are filtered out
        """
        if not self.m_reqIdFilled:
            self.checkReqs()
            self.m_reqChecked = True
        #first build specific requirements
        objReqs = []
        for libObj in libObjs:
            if libObj is None or libObj.m_module is None or libObj.m_name is None or libObj.m_name == "":
                logging.warning("error finding object during sort")
                logging.warning("obj: " + str(libObj.m_obj))
            else:
                if libObj.m_module in self.m_objSpecs and libObj.m_module in self.m_objSpecs[libObj.m_module]:
                    objSpec = self.m_objSpecs[libObj.m_module][libObj.m_name]
                    if 'required' not in objSpec or not objSpec['required']:
                        objReqs.append((libObj, set()))
                    else:
                        objReqs.append((libObj, set(objSpec['required'])))

        #using the specificly built object requirements, build the sorted and filtered list
        newLibObjList = []
        change = True
        while len(objReqs) > 0 and change:
            change = False
            for objReq in objReqs[:]:
                if not objReq[1]:   #only add elements once the requirement set is empty
                    change = True
                    newLibObjList.append(objReq[0]) #if req set is empty, add to new libObjList
                    objReqs.remove(objReq)  #remove from obj reqs
                    removeFromReqs(objReqs, objReq[0]['name'])  #remove that item from all requirement sets

        return newLibObjList

    #do not use?
    def lookupID(self, libObj):
        """
        find match for object in specs, return spec id
        """
        for index, objSpec in enumerate(self.m_objSpecs):
            objModule = parser.safeGetMoudle(libObj.m_obj.__module__)
            specModule = parser.safeGetMoudle(objSpec['call'].__module__)

            if objModule == specModule and libObj.m_obj.__name__ == objSpec['call'].__name__:
                if inspect.getsource(libObj.m_obj) == inspect.getsource(objSpec['call']):
                    return index

        logging.warning("obj not found in library")
        return None