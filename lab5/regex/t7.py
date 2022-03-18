import re

snake_case = input()
camel = re.sub('_', ' ', snake_case)
camel = camel.title()

print(re.sub(' ', '', camel))
