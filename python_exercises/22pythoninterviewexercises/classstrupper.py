class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter any String:")

    def printString(self):
        print ("UPPERCASE:",self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()


