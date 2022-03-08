import re

snake_case = input()
camel = re.search('(.+?)_([a-zA-Z])', snake_case)
camel2 = camel.group(2)[0].upper()
camelCase = re.sub('(.+?)_([a-z])', fr'\g<1>{camel2}', snake_case)

print(camelCase)