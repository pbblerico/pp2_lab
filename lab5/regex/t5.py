import re

txt = input()
x = re.findall('a.+b\W|a.+b\Z', txt)

print(x)
print("Match" if x else 'No match')