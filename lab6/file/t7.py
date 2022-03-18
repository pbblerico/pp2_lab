import os 

def exist_or_not(path1, path2):
    if os.path.exists(path2):
        copy_the_content(path1, path2)
    else:
        p = open(path2, 'x')
        copy_the_content(path1, p)

def copy_the_content(path1, path2):
     with open(path1) as f:
        with open(path2, 'w') as f1:
            for x in f:
                f1.write(x)

path1 = 'task_4.txt'
path2 = 'task_7.txt'

out = open(path2, 'r')
print(out.read())