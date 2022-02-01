#a, b = [input() for i in range(int(input()))], '@gmail.com'
#out = []
#for i in range(len(a)):
#    if b in a[i]:
#        c = len(a[i]) - len(b)
#        if c != 0:
#            out.append(a[i][:c])
#if len(out) != 0:
#    print(*out, sep='/n')

b = '@gmail.com'
for i in range(int(input())):
    a = input()
    if b in a and len(a) - len(b) != 0:
        print(a[:len(a) - len(b)])