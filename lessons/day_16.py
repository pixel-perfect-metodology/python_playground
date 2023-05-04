print('\n\nday 16\n\n')

print('# Modules')


print('')
from . import day_16_my_module
from . import day_16_my_module as mymodule


print('')
from . day_16_submodule import my_submodule


print('')
from . day_16_submodule.models import box


print('')
import importlib
module_name = 'day_16_my_module'
module_day_16_my_module = importlib.import_module('lessons.' + module_name)
module_day_16_my_module.greeting_person("Jonathan")


print('')
day_16_my_module.greeting_person("Jonathan")

from . import day_16_my_module as day_16_my_module_alias

day_16_my_module_alias.greeting_person("Jonathan")

from . day_16_my_module import greeting_person  

greeting_person("Jonathan")

from . day_16_my_module import greeting_person  as gp

gp("Jonathan")


a = mymodule.person1["age"]
print(a)


import platform

x = platform.system()
print(x)


import platform

x = dir(platform)

