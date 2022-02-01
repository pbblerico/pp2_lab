#print(input().lower())
def to_lower(s):
    out = ''
    for c in s:
        if 'A' <= c <= 'Z':
            out += chr(ord(c) + 32)
        else:
            out += c
    print(out)

s = input()
to_lower(s)