a=[12,34,2,8,9,6,8]
b=[13,23,12,4,9,8,5]
result=[]
for x in a:
    for y in b:
        if x==y:
            result.append(x)

print(result)
