n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            print(i if j == 0 else j, end=' ')
        elif i != j:
            print(0, end=' ')
        else:
            print(i ** 2, end=' ')
    if j == n - 1:
        print()