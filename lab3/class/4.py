from math import *
class point_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print('the coordinates of the point: x = {}, y = {}'.format(self.x, self.y))

    def move(self):
        a_new, b_new = input().split()
        self.x1 = int(a_new)
        self.y1 = int(b_new)
        print('new coordinates are: x = {}, y = {}'.format(a_new, b_new) )

    def dist(self):
        s = sqrt((int(self.x) - self.x1) ** 2 + (int(self.y) - self.y1) ** 2)
        print('the distance between the points: ' + '{:.2f}'.format(s))


x, y = input().split()
c = point_class(x, y)
c.show()
c.move()
c.dist()
