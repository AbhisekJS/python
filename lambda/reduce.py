from functools import reduce
lst=[2,5,43,67,20,11,12]
z=reduce(lambda x,y:x+y, lst)
'''reduce(func,sequence)'''
print(z)
