def decimal(s, i):
    if i == len(s):
        return 0
    x = int(s[i]) * 2 ** (len(s) - i - 1)
    return x + decimal(s, i + 1) 

st = input()
print(decimal(st, 0))
