#local includes

#external includes
import re
import logging
import importlib.util
import inspect
import traceback
import yaml

def safeGetMoudle(rawModule):
    justModule = rawModule.split("/")[-1]
    return justModule.replace(".py", "")

def getConfigDictFromFile(path):
    if path is not None:
        with open(path) as file:
            return yaml.load(file, yaml.FullLoader)
    return None

def safeParse(rawValue, settings = None):
    #much safe
    logging.warning("safe parse called for this value")
    logging.warning("returning raw value")
    return rawValue

def stringParse(rawValue, settings = None):
    return rawValue

def valueParse(rawValue, settings=None):
    #need to change this in someway
    return rawValue.strip()

def listParse(rawValue, settings=None):
    reDelim = ", "
    if settings is not None and 'delimiter' in settings:
        if type(settings['delimiter']) is list and len(settings['delimiter'])>0:
            reDelim = ""
            for delim in settings['delimiter']:
                reDelim += str(delim)
                reDelim += "|"
            reDelim = reDelim[:-1]
    tempList = [item.strip() for item in re.split(reDelim, rawValue)]
    return list(filter(None, tempList))

def findParseFunc(valueType):
    if valueType == "list":
        return listParse
    elif valueType == "value":
        return valueParse
    elif valueType == "string":
        return stringParse
    else:
        return safeParse

class parser:
    def __init__(self, settings=None, settingsPath=None):
        if settings is not None:
            self.m_settings = settings
        elif settingsPath is not None:
            self.m_settings = getConfigDictFromFile(settingsPath)
        else:
            #load default settings
            self.m_settings = getConfigDictFromFile("test/settings.yml")
        
        if self.m_settings is not None and 'identifierValueType' in self.m_settings:
            self.m_valueTypeDict = self.m_settings['identifierValueType']

    def parseRawValue(self, identifier, rawValue):
        vTSafe = str(self.m_valueTypeDict.get(identifier, "safe")).lower()
        parseFunc = findParseFunc(vTSafe)
        return parseFunc(rawValue, settings=self.m_settings.get(vTSafe,None))

    def loadFile(self, filePath, marker):
        objSpecs = {}
        try:
            spec = importlib.util.spec_from_file_location(filePath, filePath)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        except Exception:
            logging.error(traceback.format_exc())
        else:
            module = safeGetMoudle(filePath)
            objSpecs[module] = {}
            for funcTupl in inspect.getmembers(mod, inspect.isfunction):
                specDict = {}
                try:
                    doc = inspect.getdoc(funcTupl[1])
                except Exception:
                    logging.error(traceback.format_exc())
                else:
                    if doc is not None:
                        for line in doc.split("\n"):
                            ident, val = self.handleMarkerLine(line, marker)
                    
                            if ident is not None and val is not None:
                                if ident not in specDict:
                                    specDict[ident] = val

                    specDict['args'] = inspect.getargspec(funcTupl[1])[0]
                    specDict['call'] = funcTupl[1]
                    objSpecs[module][funcTupl[0]] = specDict
        return objSpecs

    def handleMarkerLine(self, line, marker):
        index = line.find(marker)   #find where marker is if any
        identifier = None
        value = None
        if index > -1 and index < len(line) - 1:    #if marker in line and not end of line
            split = line[index + len(marker) :].split(maxsplit=1) #split line after marker into identifer and after
            identifier = split[0].replace(":","") #remove colon if there is
            value = self.parseRawValue(identifier, split[1]) #use parser to handle raw val

        return identifier, value
        