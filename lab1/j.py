a = input().split()
print(*[a[i] for i in range(len(a)) if len(a[i]) >= 3])