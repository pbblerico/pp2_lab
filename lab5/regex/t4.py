import re

txt = input()
x = re.findall('[^A-Z][A-Z]{1}[a-z]+|\A[A-Z]{1}[a-z]+', txt)
print(x)
print("Match" if x else 'No match')