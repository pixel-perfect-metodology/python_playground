import importlib
import sys
print('sys.version', sys.version)
print('')

# from day_1 import *
# or
# import day_2
# or
# from lessons import day_17

last_day = 25

for lesson_day in range(100):
    if lesson_day == last_day:
        try:
            module_name = 'lessons.day_' + str(lesson_day)
            print('trying to import', module_name, 'module')
            importlib.import_module(module_name)
        except ModuleNotFoundError as e:
            print(repr(e))
