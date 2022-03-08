import re

txt = input()
new_txt = re.sub('[ ,.]', ':', txt)

print(new_txt)