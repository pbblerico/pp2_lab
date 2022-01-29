a = [int(i) for i in input().split()]
cnt, b = 1, True
for i in range(2, a[0] + 1):
    if a[0] % i == 0:
        cnt += 1
    if cnt > 2:
        b = False
print('Good job!' if b and a[0] <= 500 and a[1] % 2 == 0 else 'Try next time!')
    