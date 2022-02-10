data = input().split()
if len(data) == 1:
    data.append(input())
a = [int(data[1]) + 2 * i for i in range(int(data[0]))]
out = a[0]
for i in range(1, len(a)):
    out = out ^ a[i]
print(out)