from datetime import *

import time

starttime=time.perf_counter()
ldates=[]

d1=date(2016,7,10)
d2=date(2012,2,23)
d3=date(2014,11,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort(reverse=1)

for d in ldates:
    print(d)
endtime=time.perf_counter()
k=starttime-endtime
print(f"Execution Time: {k}")