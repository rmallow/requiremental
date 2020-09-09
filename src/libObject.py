import parser

class libObject:
    def __init__(self, obj):
        self.m_obj = obj
        self.m_module = None
        self.m_name = None
        self.m_reqs = set()
        if self.m_obj is not None:
            if obj.__module__ is not None:
                self.m_module = parser.safeGetMoudle(obj.__module__)
            self.m_name = obj.__name__