print('\n\nday 19\n\n')

print('# JSON')

print('')

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"], type(y['age']), type(y), repr(y))

print('')
# some invalid JSON:
x =  '{ "name":"John", "age":30, "city":"New York"'

try:
    y = json.loads(x)
except json.decoder.JSONDecodeError as error:
    print(repr(error))


print('')

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y, type(y), repr(y))


print('')

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
# print(json.dumps(pass))  # SyntaxError: invalid syntax


print('')
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, separators=[',',':']))
print(json.dumps(x, indent=4, sort_keys=True))
