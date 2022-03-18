import os

def check(path):
    if os.path.exists(path):
        print('file exists')
        print('\tfile\'s name:', os.path.basename(path))
        print('\tfile\'s path:', os.path.dirname(path), '\n')
    else:
        print('file does not exist\n')

f = 'C:\\Users\\kar-1\\pp2\\lab6\\file\\task_3.txt'
check(f)
f1 = 'C:\\Users\\kar-1\\pp2\\lab6\\file\\task_2.txt'
check(f1)

