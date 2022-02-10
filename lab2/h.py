x, y = map(int, input().split())
closest_point = []
for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    distance = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
    closest_point.append((distance, (x1, y1)))
out = sorted(closest_point)
for i in out:
    print(*i[1])