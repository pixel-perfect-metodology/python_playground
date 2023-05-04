import importlib
import sys
print('sys.version', sys.version)
print('')

# from day_1 import *
# or
# import day_2
# or
# from lessons import day_17

# lesson_folder = 'lessons'  # basic python
# last_day = 25

lesson_folder = 'lessons_matplotlib'
last_day = 1

for lesson_day in range(100):
    if lesson_day == last_day:
        try:
            module_name = f'{lesson_folder}.day_{lesson_day}'
            print('trying to import', module_name, 'module')
            importlib.import_module(module_name)
        except ModuleNotFoundError as e:
            print(repr(e))
