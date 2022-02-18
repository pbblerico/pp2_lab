def solve(numheads, numlegs):
    if numheads > numlegs or numlegs % 2 != 0:
        print('no solution')
        return
    rabbits = chickens = 0
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    print('rabbits: ' + str(rabbits) + '\n' + 'chickens: ' + str(chickens))

heads, legs = map(int, input().split())
solve(heads, legs)