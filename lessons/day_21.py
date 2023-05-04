print('\n\nday 20\n\n')

print('# pip')

print('')

'''
> pip list
'''

'''
> pip install camelcase
'''

'''
pip uninstall camelcase
'''

'''
> pip list
'''

import camelcase
c = camelcase.CamelCase()
txt = 'hello world'
print(c.hump(txt))

