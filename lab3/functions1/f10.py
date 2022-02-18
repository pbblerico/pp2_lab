def unique(numbers):
    out = []
    for i in numbers.split():
        if i not in out:
            out.append(i)
    print(*out)
    
unique(input())
