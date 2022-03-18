import os

for i in range(26):
    x = '{}.txt'.format(chr(ord('A') + i))
    if os.path.exists(x):
        os.remove(x)