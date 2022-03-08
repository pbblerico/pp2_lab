import re

txt = input()
x = re.findall('[a-z]+_[a-z]+', txt)

print("Match" if x else 'No match')