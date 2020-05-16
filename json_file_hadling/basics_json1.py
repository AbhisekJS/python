import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(json.dumps(y,indent=4,sort_keys=True)) 

# the output  json file using dump:
with open("a_sample_json_file.json",'w') as writefile:
    json.dump(y,writefile,indent=4,sort_keys=True)