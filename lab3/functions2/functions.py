def high_enough(movies):
    name = input('Print the name of the film to check whether it\'s rating is above 5.5:\n')
    for i in movies:
        if name in i['name']:
            print(i['imdb'] > 5.5)

def name_of_high_enough(movies):
    print('The list of films with rating above 5.5:')
    temp = []
    for i in movies:
       if i['imdb'] > 5.5:
           temp.append(i['name'])
    print(*temp, sep=', ')

def one_genre(movies):
    genre = input('Type the category you need:\n')
    sep = []
    for i in movies:
        if genre in i['category']:
            sep.append(i['name'])
    print('The movies of {} category: '.format(genre), end='')
    print(*sep, sep=', ')

def the_average(movies):
    total = 0
    for i in movies:
        total += i['imdb']
    print('{0:.1f}'.format(total/len(movies)))

def the_average_of_category(movies):
    genre = input('Which category\'s average rating you want to know?\n')
    total = cnt = 0
    for i in movies:
        if genre in i['category']:
            cnt += 1
            total += i['imdb']
    print('{0:.1f}'.format(total / cnt))

