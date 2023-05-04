print('\n\nday 2\n\n')

# random package
import random
print('random.randrange(1, 10)', random.randrange(1, 10))

# multiline string - option 1
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print('\n', 'multiline string (option 1):', a)

# multiline string - option 2
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print('\n', 'multiline string (option 2):', a)

# Looping Through a String
for x in "banana":
    print(x)

# string length
a = "Hello, World!"
print('string length:', len(a))

# check if the string contains the substring
txt = "The best things in life are free!"
print('"free" in txt:', "free" in txt)
print('"expensive" not in txt:', "expensive" not in txt)


# slicing strings
print('\n')
print('Slicing Strings')
print('')

sentence = "Hello, World!"
print('sentence', sentence)
print('get a char by index')
print('sentence[2]', sentence[2])
print('sentence[-5]', sentence[-5])
print('slicing strings')
print('sentence[2:5]', sentence[2:5])
print('sentence[:5]', sentence[:5])
print('sentence[2:]', sentence[2:])
print('sentence[-5:-2]', sentence[-5:-2])
print('')

# remove spaces from begining and ending of string
a = "   Hello, World! "
print('remove spaces from begining and ending of string')
print(f'original: "{a}"')
print(f'cleaned: "{a.strip()}"')  # returns "Hello, World!"
print('')

a = "Hello, World!"
print(a, 'a.split(",")', a.split(","))  # returns ['Hello', ' World!']

print('a.replace("H", "J")', a.replace("H", "J"))
print('a.upper()', a.upper())
print('a.lower()', a.lower())
