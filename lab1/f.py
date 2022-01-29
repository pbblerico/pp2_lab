a = [int(input()) for i in range(int(input()))]
for i in range(len(a)):
    if a[i] <= 10:
        print('Go to work!')
    elif a[i] <= 25:
        print('You are weak')
    elif a[i] <= 45:
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')
