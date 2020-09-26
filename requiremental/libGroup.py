#local includes
from . import library
from .libObject import libObject

#external includes
import logging

"""
Group of lib objects, correspond to a library
"""

class libGroup():
    def __init__(self, library=None):
        self.m_library = library
        self.m_sorted = True
        self.m_objs = []

    def insert(self, obj):
        if obj is not None:
            libObj = None
            if not isinstance(obj, libObject):
                libObj = libObject(obj)
            else:
                libObj = obj
                
            if libObj.m_module is None or libObj.m_name is None:
                logging.warning("error creating libObj from obj:")
                logging.warning(obj)
    
            self.m_objs.append(libObj)
            self.m_sorted = False


    def sort(self):
        self.m_objs = self.m_library.reqSort(self.m_objs)
        self.m_sorted = True
        
    def getObjs(self):
        if not self.m_sorted:
            self.sort()
        return self.m_objs

    def changeLibrary(self, library):
        self.m_library = library
        self.sort()

    def prettyPrint(self):
        for obj in self.m_objs:
            print(str(obj.m_module) + "." + str(obj.m_name))