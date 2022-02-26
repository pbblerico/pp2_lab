def decr(n):
    ans = []
    for i in range(n, -1, -1):
        ans.append(i)
    return ans

print(*decr(int(input())))