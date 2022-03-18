from time import sleep

time = int(input())
ms = int(input())
sleep(ms/1000)
print(f'Square root of {time} after {ms} miliseconds is {pow(time, 0.5)}')