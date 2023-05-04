print('\n\nday 3\n\n')

if True:
    pass

print('')
print('Strings - Format')

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print('''
```python
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
```
''')
print(myorder.format(quantity, itemno, price))
print('')

print('''
```python
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
```
''')
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# help('FORMATTING') - for more details
print('')

# replace and remove symbols from a string
print('replace and remove symbols from a string by replacement dict (table)')
txt = "Good night Sam!"

x = "mSa"
y = "eJo"
z = "odnght"

mytable = str.maketrans(x, y, z)

print(txt.translate(mytable))
print(mytable)

print('')


txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
x = txt.partition("bananas")
print(x)
print('')


a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
print('')


