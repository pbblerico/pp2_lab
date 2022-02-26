def prime(l):
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            check = True
            a, b = l[i], l[j]
            print(a, b)
            if b > a: 
                a, b = b, a
            for k in range(2, b + 1):
                if a % k == 0 and b % k == 0:
                    check = False
                    print(check)
                    break
            if check:
                print(a, b)

a = [int(i) for i in input().split()]
prime(a)