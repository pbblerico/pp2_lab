from math import *
def polygon_area(side_num, side_len):
    apothem = side_len / (2 * tan(radians(180/side_num)))
    area = 0.5 * side_len * side_num * apothem
    return area

n, s = map(int, input().split())
print('{:.2f}'.format(polygon_area(n, s)))


