def has_33(l):
    print(l)
    if '3' not in l: return False
    for i in len(l):
        if l[i] == '3':
            return True
    return False

three_neighbours = input().split()
print(has_33(three_neighbours))
