from datetime import date
import time

ldates = []

d1=date(2016,7,10)
d2=date(2012,2,23)
d3=date(2014,11,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort(reverse=1)

time.sleep(5)

for d in ldates:
    print(d)