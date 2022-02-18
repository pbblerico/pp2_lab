from random import random
def compare(ans, guess):
    if ans == guess: return 1
    elif ans > guess: return 2
    else: return 0

def check(ans, guess):
    if compare(ans, guess) == 1:
        print()

print('Hello! What is your name?')
name = input()

print('Well, {}, I am thinking of a number between 1 and 20.'.format(name))
answer, cnt = random.randint(0, 20), 0

while(1):
    cnt += 1
    print('Take a guess.')
    my_try = int(input())
    if answer == my_try:
        print('{}Good job, {}! You guessed my number in {} guesses!'.format('\n', name, cnt))
        break
    else:
        print('')
