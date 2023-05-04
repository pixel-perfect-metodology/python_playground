import os
print('\n\nday 25\n\n')

print('# File Handling')

print('')
f = open('./lessons/day_25_demo_file.txt', 'w')
txt = '''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''
f.write(txt)
f.close()

f = open("./lessons/day_25_demo_file.txt", 'rt')
print(repr(f.read()))
f.seek(0)
print('')
print(f.read())
f.close()

print('')
print('')
f = open("lessons/day_25_demo_file.txt", 'rt')
print(repr(f.read(10)))
f.seek(0)
print('')
print(f.read(10))
print('')
print(f.read(10))
f.close()

print('')
print('')
f = open("lessons/day_25_demo_file.txt", "r")
print(f.readline())
print(f.readline())
f.close()

print('')
print('')
f = open("lessons/day_25_demo_file.txt", "r")
for x in f:
    print(x)

print('')
print('')
print('')

# f = open("lessons/day_25_demo_file_2.txt", "a")  # append content
f = open("lessons/day_25_demo_file_2.txt", "w")  # overwrite content
f.write("Now the file has more content!")
f.close()

print('')
# open and read the file after the appending:
f = open("lessons/day_25_demo_file_2.txt", "r")
print(f.read())
f.close()

print('')
file_path = 'lessons/day_25_demo_file.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"The file {file_path} does not exist")

file_path = "lessons/day_25_demo_file_2.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"The file {file_path} does not exist")


print('')
file_folder = './lessons/subfolder'
file_path = f'{file_folder}/day_25_demo_file_3.txt'
try:
    os.mkdir(file_folder)
except Exception as e:
    print(repr(e), file_folder)

f = open(file_path, 'w')
txt = '''
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
'''
f.write(txt)
f.close()


try:
    os.rmdir(file_folder)
except OSError as e:
    print(repr(e))
    print(file_folder)
    print(os.listdir(file_folder))
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"The file {file_path} does not exist")
finally:
    os.rmdir(file_folder)
