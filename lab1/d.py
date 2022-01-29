z, x = int(input()), input()
if x == 'k':
    c = "{:." + input() + "f}"
    print(c.format(z / 1024))
else:
    print(z * 1024)