import re

txt = input()
x = re.findall('ab{2}b?\Z|ab{2}b?\s', txt)

print(x)
print("Match" if x else 'No match')