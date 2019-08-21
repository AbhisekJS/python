x=675
def scope(k):
    x=500
    y= 300
    print('local value x',x)
    print(globals()['x'])
    sum= k + (globals()['x'])
    return(sum)
print (x)
print(scope(55))
z=scope
z(20)
