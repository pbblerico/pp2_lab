class evens:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self 
        
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 2
            return cur
        raise StopIteration
       
out = evens(int(input()))
myiter = iter(out)
a = list()

for x in myiter:
    a.append(x)

print(*a, sep = ', ')
