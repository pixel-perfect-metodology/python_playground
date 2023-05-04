print('\n\nday 20\n\n')

print('# RegEx')

print('')
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(txt)
print(x)

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.search("\\s", txt)
print("The first white-space character is located in position:", x.start())
print(x)

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.split("\\s", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.split("\\s", txt, 1)
print(x)

import re
txt = "The rain in Spain"
x = re.sub("\\s", "9", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.sub("\\s", "9", txt, 2)
print(x)

import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
print(x.span())
print(x.string)
print(x.group())

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
