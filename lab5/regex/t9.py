import re

txt = input()
space = re.sub('([^A-Z]?)([A-Z])', r'\1 \2', txt)
space = re.sub('  ', ' ', space)
space = re.sub('\A ', '', space)
print(space)


