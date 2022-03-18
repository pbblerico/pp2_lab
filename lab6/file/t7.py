import os 

def copy_the_content(path1, path2):
    f = open(path1, 'r')
    with open(path2, 'w') as f1:
        for x in f:
            f1.write(x)

path1 = 'task_4.txt'
path2 = 'task_7.txt'

copy_the_content(path1, path2)
out = open(path2, 'r')
print(out.read())