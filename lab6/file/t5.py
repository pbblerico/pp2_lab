import os

def exist_or_not(lst, path):
    if os.path.exists(path):
        list_to_file(lst, path)
    else:
        p = open(path, 'x')
        list_to_file(lst, p)

def list_to_file(lst, path):
    with open(path, 'w') as f:
        for x in lst:
            f.write('%s\n' % x)

lst = input().split()
path = 'task_5.txt'
exist_or_not(lst, path)
out = open('task_5.txt', 'r')
print(out.read())
