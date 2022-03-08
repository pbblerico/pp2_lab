import re

camelCase = input()
snake_case = re.sub('(.+?)([A-Z])', r'\g<1>_\g<2>', camelCase)
print(snake_case.lower())

