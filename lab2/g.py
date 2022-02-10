from collections import defaultdict
def value():
    return 0

demons, kills = defaultdict(value), defaultdict(value)
alive = 0
for _ in range(int(input())):
    demon_name, weakness = input().split()
    demons[weakness] += 1

for _ in range(int(input())):
    name, ability, kills_left = input().split()
    kills[ability] += int(kills_left)

for i in demons:
    alive += ((demons[i] - kills[i]) * (demons[i] > kills[i]) if i in kills else demons[i])
    
print('Demons left:', alive)
       


