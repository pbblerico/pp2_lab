import os

path = os.getcwd()
print(*[name for name in os.listdir(path)])
