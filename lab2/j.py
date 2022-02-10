password, strong_pass = [input() for i in range(int(input()))], []
for i in password:
    test1, test2, test3 = False, False, False
    for c in i:
        if '0' <= c <= '9':
            test1 = True
        if 'a' <= c <= 'z':
            test2 = True
        if 'A' <= c <= 'Z':
            test3 = True
    if test1 and test2 and test3 and i not in strong_pass:
        strong_pass.append(i)
out = sorted(strong_pass)
print(len(strong_pass), *out, sep='\n')

    