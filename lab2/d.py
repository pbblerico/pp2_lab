n = int(input())
for i in range(1, n + 1):
    print('.' * (n - i) + '#' * i if n % 2 == 1 else '#' * i + '.' * (n - i))