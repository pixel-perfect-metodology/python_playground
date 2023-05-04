print('\n\nday 11\n\n')

print('# Functions')


def my_function():
    print("Hello from a function")


def my_function():
    print("Hello from a function 2")


my_function()


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


def my_function(fname, lname):
    print(fname + " " + lname)


# my_function("Emil")  # TypeError: my_function() missing 1 required positional argument: 'lname'


def my_function(*kids):  # *args  # Arbitrary Arguments, *args
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child3="Tobias", child2="Linus")


def my_function(**kid):  # **kwargs  # Arbitrary Keyword Arguments, **kwargs
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
    pass


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print('k', k, 'result', result)
    else:
        result = 0
    return result


print('\n\nRecursion Example Results')
tri_recursion(6)


print('')
print('# Lambda function')

print('')
x = lambda a : a + 10
# x = lambda a : a + 10
print(x(5))
print((lambda a : a + 10)(5))

x = lambda a, b : a * b
# x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
# x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
# def myfunc(n):
#   return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))
