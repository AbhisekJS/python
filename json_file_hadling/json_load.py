#python program to write jsn to a file
import json

#syntax for opening an json file
with open("F:\sample data\Python\json_file_hadling\sample.json","r") as read_file:
    data=json.load(read_file)

print(json.dumps(data,indent=2,sort_keys=True))

lst=[]
for items in data['menu']:
    print(items)
print(lst.append(items))