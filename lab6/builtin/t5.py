tup = [i for i in input().split()]
tup = [0 if i == '0' or i == 'False' else i for i in tup]
print(all(tup))