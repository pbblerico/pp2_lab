import os

for i in range(26):
    x = chr(ord('A') + i)
    f = open('{}.txt'.format(x), 'x')

os.renames('t6_t8.py', 't6.py')








