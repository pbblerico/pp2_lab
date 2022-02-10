n = input()
a, max_product = input().split(), 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        max_product = max(max_product, int(a[i]) * int(a[j]))
print(max_product)
