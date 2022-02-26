a = [i for i in range(int(input()))]
res = list(filter(lambda x: x % 12 == 0, a))
print(*res)