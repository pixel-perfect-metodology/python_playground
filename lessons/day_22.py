print('\n\nday 22\n\n')

print('# Try Except')

print('')

try:
    print(x)
except:
    print("An exception occurred")

print('')

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print('')

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print('')

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print('')

try:
    # Try to open and write to a file that is not writable
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file (1)")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file (2)")


print('')


try:
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(repr(e))


print('')


try:
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except Exception as e:
    print(repr(e))
