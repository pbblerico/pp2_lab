import datetime 
import math

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
date1 = datetime.date(y1, m1, d1)
date2 = datetime.date(y2, m2, d2)

print(abs(date1 - date2).total_seconds())

