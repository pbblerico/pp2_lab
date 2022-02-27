class Shape:
    def __init__(self):
        self.area = 0

    def print_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = self.length ** 2
        
class rectangle(Shape):
    def __init__(self, a, b):
        self.length = a
        self.width = b
    
    def rec_area(self):
        self.area = self.length * self.width 

x = Square(int(input()))
x.print_area()
y = rectangle(int(input()), int(input()))
y.print_area()