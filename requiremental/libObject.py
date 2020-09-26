#local includes
from . import parser

#external includes
import collections

class libObject:
    def __init__(self, obj, details = None):
        self.m_obj = obj
        self.m_module = None
        self.m_name = None
        self.m_details = {}
        self.m_reqs = {}
        if self.m_obj is not None:
            if obj.__module__ is not None:
                self.m_module = parser.safeGetMoudle(obj.__module__)
            self.m_name = obj.__name__

        if isinstance(details, collections.Mapping):
            self.m_details = details