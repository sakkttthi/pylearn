# JavaScript object notation. 
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["age"])

# python obj to json 
a = {
    "name": 'apple', 
    "num" : 20, 
    "fruit" : 'orange'
}

b = json.dumps(a, indent=2,sort_keys=True,separators=(",","="))

print(b)