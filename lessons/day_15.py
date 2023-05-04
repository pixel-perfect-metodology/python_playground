print('\n\nday 15\n\n')

print('# Scope')

print('')


def myfunc():
    x = 300
    print(x)


myfunc()

print('')


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()


print('')

x = 300


def myfunc():
    print(x)


myfunc()

print(x)

print('')

x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)


print('')


def myfunc():
    global xx
    xx = 3000


myfunc()

print(xx)


print('')

x = 3003


def myfunc():
    global x
    x = 2002


myfunc()

print(x)

print('')
print('')
