import sys
print('\n\nday 1\n\n')

print("Hello CodeSandbox!")

print(sys.version)

print('sys.builtin_module_names', sys.builtin_module_names)
print('sys.path', sys.path)

# multi
# line
# comment
# -
# option 1


"""
multiline comment - option 2
"""

print('hello python')


casted_as_string = str(3)
casted_as_integer = int(3)
casted_as_float = float(3)
casted_as_bool = bool(3)

print(casted_as_string, casted_as_integer, casted_as_float, casted_as_bool)
print(type(casted_as_string),
      type(casted_as_integer),
      type(casted_as_float),
      type(casted_as_bool)
      )


def x(a, b, c): return a + b + c


# or as on next line
# x = lambda a, b, c : a + b + c
print(f"using lambda function x(5,6,7): {x(5,6,7)}")


# set many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# unpack a colletion
fruits = ['apple', 'banana', 'cherry']
one, two, three = fruits
print(one, two, three)

# output variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# the global keyword
def somefunc():
    global variable_x
    variable_x = 'fantastic'


somefunc()

print(f'Python is {variable_x}')


# complex numeric type
complex_x = complex(5, 7)
print(complex_x, type(complex_x))
complex_y = 4j
print(complex_y, type(complex_y))

# bytes
bytes = b"Hello"
print(bytes, type(bytes))

# byte array
byte_array = bytearray(5)
print(byte_array, type(byte_array))

# memoryview
# note: "bytes(5)"" not working in codesandbox vm
# memory_view = bytes(5)
# memory_view = memoryview(bytes(5))
# print(memory_view, type(memory_view))
# or
# x = memoryview(bytes(5))
# print(x)
# print(type(x))

# integer numbers
x = 1
y = 35656222554887711356562225548877113565622255488771135656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))
print('sys.maxsize', sys.maxsize)
print('sys.int_info', sys.int_info)
print('sys.float_info', sys.float_info)
print('sys', sys)
# ====================================================
