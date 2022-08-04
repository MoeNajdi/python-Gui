from studentClass import *
class Marks(Student):
    historyMarks = 0
    geographyMarks = 0
    def __init__(self, name, code, historyMarks, geographyMarks):
        Student.__init__(self, name, code)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks
    
    def getHistoryMarks(self):
        return self.historyMarks
    
    def getGeographyMarks(self):
        return self.geographyMarks

