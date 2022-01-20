import pizza as p
from pizza import make_pizza  # importing specific functions
# importing all functions from a module using 
# e.g from pizza import *

# the line import pizza tells python to open the file pizza.py and copy all the functions from it into this prog
# every function defined in pizza.py will now be available in making_pizzas.py.

# module_name.function()

print('*' * 20)
print("To call a function from an imported module, enter d name of d module")
print("Every function in the module will be available")
# enter the name of the module u imported, pizza foloowed by the name of the function, make_pizza(), seperated by a dot
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'module', 'extra cheese')

print('*' * 20)
print("Importing a specific function in the module ")
print("from module_name import function_name")

#import as many functions, seperated by commas

from pizza import make_pizza
make_pizza(15, 'ajebutter')
make_pizza(20, 'Ajeju', 'Ewa Agoing', 'Egusi')

print('\n')
print(f"-" * 20)
print("Using as to give a function an Alias")
# when function is conflicting with another name or if it is too long
p.make_pizza(50, 'oyato')
p.make_pizza(100, 'good', 'better', 'worse')

