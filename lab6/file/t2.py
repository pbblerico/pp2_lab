import os

def check(path):
    print('The file exists' if os.access(path, os.F_OK) else 'The file doesn\'t exist')
    print('The file is readable' if os.access(path, os.R_OK) else 'The file isn\'t readable')
    print('The file is writable' if os.access(path, os.W_OK) else 'The file isn\'t writable')
    print('The file is executable\n' if os.access(path, os.F_OK) else 'The file isn\'t executable\n')


code = 't8.py'
txt = 'task_2.txt'
picture = 'C:\\Users\\kar-1\\OneDrive\\Изображения\\Снимки экрана\\2021-12-19 (2).png'
check(code)
check(txt)
check(picture)