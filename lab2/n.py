n, a = int(input()), []
while n != 0:
    a.append(n)
    n = int(input())
for i in range(len(a) // 2 + (len(a) % 2 == 1)):
    sum = a[i]
    #if i != len(a) - i - 1:
    sum = a[i] + a[n - i - 1]
    print(sum, end=' ')