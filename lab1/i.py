a, b = [input() for i in range(int(input()))], '@gmail.com'
for i in range(len(a)):
    if b in a[i]:
        c = len(a) - len(b)
        print(a[i][:c])