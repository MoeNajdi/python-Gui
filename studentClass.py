class Student:
    name=""
    code = 0
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def printName(self):
        return self.name
    
    def printCode(self):
        return self.code