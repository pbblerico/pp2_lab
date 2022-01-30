#a, b = [input() for i in range(int(input()))], '@gmail.com'
#out = []
#for i in range(len(a)):
#    if b in a[i]:
#       c = len(a[i]) - len(b)
#        out.append(a[i][:c])
##if len(out) != 0:
#    print(*out, sep='/n')

b = '@gmail.com'
for i in range(int(input())):
    s = ''
    a = input()
    if b in a:
        s = a[:len(a) - len(b)]
    if len(s) != 0:
        print(s)