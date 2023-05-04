print('\n\nday 5\n\n')

# List
print('# list')
orig_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
edible_list = []


def reset_edible_list():
    global edible_list
    edible_list = orig_list.copy()
    print('')
    print(edible_list)


# get list item or sublist
reset_edible_list()
print('edible list', edible_list)

print(edible_list[1])
print(edible_list[-1])
print(edible_list[2:5])
print(edible_list[:4])
print(edible_list[2:])
print(edible_list[-4:-1])

if "apple" in edible_list:
    print("Yes, 'apple' is in the fruits list")

# bulk insert/remove list items
reset_edible_list()
edible_list[1] = "blackcurrant"
print(edible_list)

reset_edible_list()
edible_list[1:2] = ["blackcurrant", "watermelon", 'kiwi']
print(edible_list)

reset_edible_list()
edible_list[1:5] = ["blackcurrant", "watermelon"]
print(edible_list)

reset_edible_list()
edible_list[1:3] = []
print(edible_list)

reset_edible_list()
edible_list[1:] = []
print(edible_list)

reset_edible_list()
edible_list.insert(2, "watermelon")
print(edible_list)

a = [1, 2, 4]
# b=a #accessing the list by link
b = a.copy()
a[1] = 12
b[2] = 33
print(a, b)

# append
reset_edible_list()
edible_list.append("orange")
print(edible_list)

# extend list
print('')
the_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
print(the_list)
print(tropical)
the_list.extend(tropical)
print(the_list)

print('')
the_list = ["apple", "banana", "cherry"]
tropical_turplet = ("kiwi", "orange")
frozen_set = {"frozen_kiwi", "frozen_orange"}
from_book_dictionary = {"vegetable": 'onion', "fruit": 'ananas'}
print(the_list)
print(tropical_turplet)
print(frozen_set)
print(from_book_dictionary)
the_list.extend(tropical_turplet)
the_list.extend(frozen_set)
the_list.extend(from_book_dictionary)
print(the_list)

print('')
print([1, 2, 3]+[4, 5, 6])

the_list = []


def reset_the_list():
    print('')
    global the_list
    the_list = ["apple", "banana", "cherry"]
    print(the_list)


# remove item
reset_the_list()
the_list.remove("banana")
print(the_list)

reset_the_list()
the_list.pop(1)
print(the_list)

reset_the_list()
the_list.pop()
print(the_list)

reset_the_list()
del the_list[0]
print('del the_list[0]')
print(the_list)

reset_the_list()
del the_list
print('del the_list')
try:
    print(the_list)
except NameError:
    print('the_list is not defined')

if 'the_list' in vars() or 'the_list' in globals():
    print(the_list)
else:
    print('the_list is not defined')

# if 1> 0:
#     x = 2
#     print(locals())
#    # print(vars())
#    # print(globals())

print('')
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print('thislist.clear()')
print(thislist)

print('')
print('')
print('## loop through a list')
# loop through a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

print('')
for x in thislist:
    print(x)

print('')
for i in range(len(thislist)):
    print(thislist[i])

print('')
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

print('')
print('## looping using list comprehension')
thislist = ["apple", "banana", "cherry"]
print('[print(x) for x in thislist]')
[print(x) for x in thislist]
new_list = [print(x) for x in thislist]
print('new_list', new_list)


print('')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list_1 = []
new_list_2 = []
print('fruits', fruits)
print('newlist', new_list_1)

for x in fruits:
    if "a" in x:
        new_list_1.append(x)

# syntax of list comprehension
# newlist = [expression for item in iterable if condition == True]
new_list_2 = ['frozen_' + x for x in fruits if "a" in x]

new_list_3 = [x for x in fruits if x != "apple"]

print('new_list_1', new_list_1)
print('new_list_2', new_list_2)
print('new_list_3', new_list_3)

print('')
print(range(10), type(range(10)))
print([x for x in range(10)], type([x for x in range(10)]))

print('')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
newlist = [x.upper() for x in fruits]
print(newlist)

print('')
print(fruits)
newlist = ['hello' for x in fruits]
print(newlist)

print('')
print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


print('')
print('## sort lists')
# import random
thislist = ['aab', 'aac', 'ccc', 'abb', 'aaa']
# random.seed(10)
# random.shuffle(thislist)
print(thislist)
thislist.sort()
print(thislist)

print('')
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)

print('')
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse=True)
print(thislist)

print('')
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse=1)
print(thislist)


print('')
print('## Customize Sort Function')


def sort_comparator(val):
    return abs(val - 50)


thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(key=sort_comparator)
print(thislist)


print('')
print('# case sensitive sort (default behaviour)')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print(thislist)


print('')
print('## Case Insensitive Sort')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort(key=str.lower)
print(thislist)

print('')
print('## Reverse Order')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.reverse()
print(thislist)


print('')
print('')
print('# copy list')

print('')
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('mylist = thislist.copy()')
mylist = thislist.copy()
print(mylist)

print('')
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('mylist = list(thislist)')
mylist = list(thislist)
print(mylist)


print('')
print('')
print('## Join Two Lists')

print('')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1)
print(list2)

print('')
list3 = list1 + list2
print('list3 = list1 + list2')
print(list3)


print('')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print('''for x in list2:
    list1.append(x)''')
print(list1)


print('')
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print('list1.extend(list2)')
print(list1)
