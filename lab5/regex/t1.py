import re

txt = input()
x = re.findall('\Aab*|\sab*', txt)

print(x)
print("Match" if x else 'No match')