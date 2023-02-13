import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

x = {
    "name" : "prabati",
    "age" : "35",
    "address" : "Dhading"
}

y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps("hello parbati"))
print(json.dumps("your age is 35"))
print(json.dumps(True))