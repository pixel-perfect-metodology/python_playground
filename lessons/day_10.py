print('\n\nday 10\n\n')

print('# Loops')

print('')
print('## While Loops')

print('')
i = 1
while i < 6:
    print(i)
    i += 1

print('')
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print('')
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print('')
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


print('')
print('')
print('## For Loops')

print('')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print('')
for x in "banana":
    print(x)

print('')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print('')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print('')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('')
for x in range(6):
    print(x)

print('')
for x in range(2, 6):
    print(x)

print('')
for x in range(2, 30, 3):
    print(x)

print('')
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print('')
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

print('')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

print('')
for x in [0, 1, 2]:
    pass

print('')
