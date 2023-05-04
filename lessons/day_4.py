print('\n\nday 4\n\n')

# Booleans
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# object in this case, evaluates to False,
# and that is if you have an object
# that is made from a class with a __len__ function
# that returns 0 or False


class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
print('')

# logical operators
x = 2
print('x =', x)
if x < 5 and x < 10:
    print('x < 5 and x < 10', True)
else:
    print('x < 5 and x < 10', False)

if 5 > x < 10:
    print('5 > x < 10', True)
else:
    print('5 > x < 10', False)

# membership operators
x = ["apple", "banana"]
print('x =', x, '"banana" in x', "banana" in x)
