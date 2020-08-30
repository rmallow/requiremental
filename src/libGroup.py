import library

"""
Group of lib objects, correspond to a library
"""

class libGroup():
    def __init__(self, library=None):
        self.m_library = library
        self.m_sorted = True
        self.m_objs = []

    def insert(self, obj):
        if obj.m_id is None:
            obj.m_id = self.m_library.lookupId(obj)
        self.m_objs.append(obj)
        self.m_sorted = False

    def sort(self):
        self.m_objs = self.m_library.sort(self.m_objs)
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