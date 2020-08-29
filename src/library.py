import parser

class library():
    def __init__(self, parser):
        self.m_objs = []
        self.m_parser = parser

    def loadFile(self, filePath, marker):
        self.m_objs.extend(self.m_parser.loadFile(filePath,marker))
        print(self.m_objs)
                    

