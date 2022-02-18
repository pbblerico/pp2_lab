def spy_game(lst):
    temp = ''
    for i in lst:
        if i == '0' or i == '7':
            temp +=  i
    if '007' in temp: return True
    return False

l = input().split()
print(spy_game(l))