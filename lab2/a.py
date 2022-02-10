jump = input().split()
index = the_farthest = 0
while(1):
    if index == len(jump):
        print(1)
        break
    if index > the_farthest:
        print(0)
        break
    the_farthest = max(index + int(jump[index]), the_farthest)
    index += 1
    



