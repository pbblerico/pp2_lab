s, c = input(), input()
if s.count(c) == 1:
    print(s.find(c))
else:
    print(s.find(c), s.rfind(c))