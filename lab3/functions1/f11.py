def palindrome(str):
    str_rev = ''
    for i in range(len(str) - 1, -1, -1):
        str_rev += str[i]
    print(str_rev == str)

palindrome(input())