class up_string:
    def __init__(self, getString):
        self.getString = getString.upper()
    
    def printString(self):
        print(self.getString)

p = up_string(input())
p.printString()
