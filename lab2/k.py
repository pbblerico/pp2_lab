word, unique = [i for i in input().split()], []
for i in word:
    if i[-1] == '?' or i[-1] == '.' or i[-1] == ',' or i[-1] == '!':
        i = i[:-1]
    if i not in unique:
        unique.append(i)
unique = sorted(unique)
print(len(unique), *unique, sep='\n')

