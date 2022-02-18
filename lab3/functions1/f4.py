def filter_prime(l):
    real_primes = lambda k: [int(i) for i in l.split() if is_prime(int(i)) == 1]
    print(*real_primes)

def is_prime(check):
    for i in range(2, check):
        if check % i == 0:
            return 0
    if check != 0: return 1
    else: return 0

filter_prime(input())