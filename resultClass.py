from marksClass import *
class Results(Marks):
    total = 0
    percentage = 0
    def __init__(self, name, code, historyMarks, geographyMarks):
        Marks.__init__(self,name, code, historyMarks, geographyMarks)
        self.total = self.geographyMarks + self.historyMarks
        self.percentage = (self.geographyMarks + self.historyMarks) /200 *100

    def getTotal(self):
        return self.total
    def getPercentage(self):
        return self.percentage