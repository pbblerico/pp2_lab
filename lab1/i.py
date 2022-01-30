a, b = [input() for i in range(int(input()))], '@gmail.com'
out = []
for i in range(len(a)):
    if b in a[i]:
        c = len(a[i]) - len(b)
        out.append(a[i][:c])
print(*out, sep='/n')