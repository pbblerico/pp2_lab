from itertools import permutations
def permutation(st):
    l = permutations(st)
    for i in l:
        print(''.join(i))

st = input()
permutation(st)
