print('\n\nday 7\n\n')

print('# Sets')

myset = {"apple", "banana", "cherry"}
print('myset', myset)

print('')
thisset = {"apple", "banana", "cherry", "apple"}
print('''
thisset = {"apple", "banana", "cherry", "apple"}
''')
print('thisset', thisset)

print('')
print('')
print('## True and 1 is considered the same value:')

thisset = {"apple", "banana", "cherry",  1, True, 2}
# {1, 2, 'apple', 'cherry', 'banana'}

# thisset = {"apple", "banana", "cherry", True, 1,  2}
# {True, 2, 'apple', 'cherry', 'banana'}

print('''
thisset = {"apple", "banana", "cherry", True, 1, 2}
''')
print('thisset', thisset)

print('')
print('##Get the Length of a Set')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)
print('len(thisset)', len(thisset))

print('')
print('## Access Set Items')

thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)

print('''
for x in thisset:
  print(x)
''')
for x in thisset:
    print(x)

print('')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)
print('"banana" in thisset', "banana" in thisset)


print('')
print('')
print('# Add Set Items')

print('')
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print('thisset.add("orange")')
print('thisset', thisset)

print('')
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print('thisset', thisset)
print('tropical', tropical)

thisset.update(tropical)
print('thisset.update(tropical)')
print('thisset', thisset)

print('')
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
print('thisset', thisset, type(thisset))
print('mylist', mylist, type(mylist))

print('')
thisset.update(mylist)
print('thisset.update(mylist)')
print('# argument can be any iterable object (tuples, lists, dictionaries etc.)')
print('thisset', thisset)


print('')
print('')
print('## Remove Item')

print('')
print('Remove "banana" by using the remove() method:')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)

thisset.remove("banana")
print('thisset.remove("banana")')
print('### Note: If the item to remove does not exist, remove() will raise an error.')
print('thisset', thisset)

print('')
print('## Remove "banana" by using the discard() method:')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)
thisset.discard("banana")
print('thisset.discard("banana")')
print('### Note: If the item to remove does not exist, discard() will NOT raise an error.')
print('thisset', thisset)

print('')
print('## Remove a random item by using the pop() method:')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)
x = thisset.pop()
print('x = thisset.pop()')
print('x', x)
print('thisset', thisset)

print('')
print('## The clear() method empties the set:')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)
thisset.clear()
print('thisset', thisset)

print('')
print('The del keyword will delete the set completely:')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)

print('del thisset')
del thisset
# print(thisset)  # NameError: name 'thisset' is not defined


print('')
print('')
print('# ')
thisset = {"apple", "banana", "cherry"}
print('thisset', thisset)

print('''
for x in thisset:
  print(x)
''')

for x in thisset:
    print(x)


print('')
print('')
print('# Join Sets')

print('')
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print('set3 = set1.union(set2)')
print('set3', set3)

print('')
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print('set1.update(set2)')
print('set1', set1)

print('')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print('x.intersection_update(y)')
print('x', x)

print('')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print('z = x.intersection(y)')
print('z', z)

print('')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print('x.symmetric_difference_update(y)')
print('x', x)

print('')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print('z = x.symmetric_difference(y)')
print('z', z)

print('')
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print('z = x.symmetric_difference(y)')
print('z', z)
