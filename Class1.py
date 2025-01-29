class Myclass:
    def __init__(self):
        self.strng = ""
    def getstring(self):
        self.strng = input()
    def printString(self):
        print(self.strng.upper())
a = Myclass()
a.getstring()
a.printString()