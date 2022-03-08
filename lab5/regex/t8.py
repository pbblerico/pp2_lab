import re

txt = input()
new_text = re.split('[A-Z]', txt)
print(new_text)