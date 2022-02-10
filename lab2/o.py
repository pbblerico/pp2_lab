s, sum = input().split('+'), 0
to_digit = {'ZER' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOU' : 4, 'FIV' : 5, 'SIX' : 6, 'SEV' : 7, 'EIG' : 8, 'NIN' : 9}
to_letter = {0 : 'ZER', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOU', 5 : 'FIV', 6 : 'SIX', 7 : 'SEV', 8 : 'EIG', 9 : 'NIN'}
for i in range(len(s)):
    temp_num = 0
    for j in range(0, len(s[i]), 3):
        temp = s[i][j:j+3]
        temp_num = temp_num * 10 + to_digit[temp]
    sum += temp_num
sum, out = str(sum), ''
for c in sum:
    out += to_letter[int(c)]
print(out)