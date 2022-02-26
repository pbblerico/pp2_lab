def squares(n):
    lst = [i ** 2 for i in range(n)]
    return lst

n = int(input())
print(*squares(n))