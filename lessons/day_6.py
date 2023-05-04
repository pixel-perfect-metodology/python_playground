print('\n\nday 6\n\n')

print('# Tuples')
mytuple = ("apple", "banana", "cherry")
print('mytuple = ("apple", "banana", "cherry")')
print('mytuple[1]', mytuple[1])
print('mytuple[-1]', mytuple[-1])
print('mytuple[-2]', mytuple[-2])

# mytuple[1] = 'qwd' #TypeError: 'tuple' object does not support item assignment

print('')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print('thistuple', thistuple)
print('thistuple[2:5]', thistuple[2:5])
print('thistuple[:4]', thistuple[:4])
print('thistuple[2:]', thistuple[2:])
print('thistuple[-4:-1]', thistuple[-4:-1])

print('')
print('''if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")''')
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

print('')
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print('len(thistuple)', len(thistuple))

print('')
print('## Create Tuple With One Item')
thistuple = ("apple",)
print('thistuple = ("apple",)')
print(type(thistuple))

# NOT a tuple
print('')
print('#NOT a tuple')
thistuple = ("apple")
print('thistuple = ("apple")')
print(type(thistuple))

print('')
print('## create a tuple from a tuple')
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print('thistuple = tuple(("apple", "banana", "cherry"))')
print(thistuple)
print(type(thistuple))
tuple_one = ("apple", "banana", "cherry")
tuple_two = tuple(tuple_one)
print(tuple_one, tuple_two)
print(type(tuple_one), type(tuple_two))
print('tuple_one == tuple_two', tuple_one == tuple_two)


print('')
print('')
print('## change tuple values')
print('## (by convert it to list and convert to back to tuple)')

x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print('''
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
''')
print(x)


print('')
print('')
print('## add items')
print('## (by using list)')

thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print('''
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
''')

print(thistuple)

print('')
print('## (by using + operator)')
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print('''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
''')

print(thistuple)


print('')
print('')
print('# Remove Items')

thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print('''
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
''')

print(thistuple)

print('')
print('## the "del" keyword can delete the tuple completely')
thistuple = ("apple", "banana", "cherry")
del thistuple
print('''
del thistuple
''')
# print(thistuple)  # NameError: name 'thistuple' is not defined
# this will raise an error because the tuple no longer exists

print('')
print('')
print('# Unpacking a Tuple')

fruits = ("apple", "banana", "cherry")
print('fruits', fruits)

(green, yellow, red) = fruits

print('''
(green, yellow, red) = fruits
''')

print('"green"', green)
print('"yellow"', yellow)
print('"red"', red)

print('')
print('')
print('# Using Asterisk* to unpack a tuple')

fruits = ("apple", "banana", "cherry", 'watermelon', 'banana')
(green, yellow, *red) = fruits

print('''
(green, yellow, *red) = fruits
''')

print('"green"', green)
print('"yellow"', yellow)
print('"red"', red)

print('')
(green, *tropic, red) = fruits

print('''
(green, *tropic, red) = fruits
''')

print('"green"', green)
print('"tropic"', tropic)
print('"red"', red)


print('')
print('# loop through a tuple')

thistuple = ("apple", "banana", "cherry")
print('thistuple', thistuple)

print('')
for x in thistuple:
    print(x)

print('''
for x in thistuple:
  print(x)
''')

print('')
for i in range(len(thistuple)):
    print(thistuple[i])

print('''
for i in range(len(thistuple)):
  print(thistuple[i])
''')

print('')
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print('''
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
''')

print('')
print('')
print('# Join Tuples')

print('')
print('## Join Two Tuples')

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print('''
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
''')
print('tuple3', tuple3)

print('')
print('## Multiply Tuples')

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print('''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
''')
print('mytuple', mytuple)

print('len(mytuple)', len(mytuple), 'type(mytuple)', type(mytuple))
print("mytuple.count('banana')", mytuple.count('banana'))
print("mytuple.count('band')", mytuple.count('band'))

print('')
print("mytuple.index('banana')", mytuple.index('banana'))

print('''
try:
    mytuple.index('band')  # ValueError: tuple.index(x): x not in tuple
except ValueError:
    print('value "band" is not found')
''')

try:
    mytuple.index('band')  # ValueError: tuple.index(x): x not in tuple
except ValueError:
    print('value "band" is not found')
