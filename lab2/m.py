calendar = []
while(1):
    date = input().split()
    if len(date) == 1:
        break
    calendar.append(date)
sorted_calendar = sorted(calendar, key = lambda k: [k[2], k[1], k[0]])
for i in sorted_calendar:
    print(*i)