shelf, taken = [], []
for _ in range(int(input())):
    action = input().split()
    if len(action) == 1 and len(shelf) == 0:
        continue 
    elif len(action) == 1:
        taken.append(shelf[0])
        shelf.remove(shelf[0])
    else:
        shelf.append(action[1])
print(*taken)
