from functools import reduce
lst=[10,20,43,5,69,98,12,35]
res= reduce(lambda x,y:x*y,lst)
'''filter'''
print (res)

lst=[10,20,43,5,69,98,12,35]
y=1
for x in lst:
    y=y*x
print(y)