def trapezoid_area(height, base1, base2):
    area = 0.5 * height * (base1 + base2)
    return area

h, b1, b2 = map(int, input().split())
print(trapezoid_area(h, b1, b2))