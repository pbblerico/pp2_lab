a = 0
def decimal(s, i):
    if i == len(s):
        return 1
    else:
        c = 2 ** int(len(s) - int(s[i]) - 1)
        global a += c 
        decimal(s, i + 1)
    
    return a

s = input()
decimal(s, 0)

