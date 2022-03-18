import os 

cnt = 0
with open('task_4.txt') as f:
    for i in f:
        cnt += 1

print(f'There\'re {cnt} lines in the file')