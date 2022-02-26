def squares(a, b):
    for i in range(a, b):
        yield i ** 2

a, b = map(int, input().split())
out = squares(a, b)
for i in out:
    print(i, end = ' ')