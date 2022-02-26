def sec_max(l):
    t = l[0]
    for i in range(1, len(l)):
        if l[i] > t: t = l[i]
    print(t)


a = [int(i) for i in input().split()]
sec_max(a)