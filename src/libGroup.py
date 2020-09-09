import library
from libObject import libObject
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
            if obj is not libObject:
                libObj = libObject(obj)
            else:
                libObj = obj
            
            if libObj.m_id is None and self.m_library is not None:
                libObj.m_id = self.m_library.lookupID(libObj)
                
            if libObj.m_id is None:
                logging.warning("object not found in specified library")
    
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
        for obj in self.m_objs:
            obj.m_id = self.m_library.lookupId(obj)
        self.sort()