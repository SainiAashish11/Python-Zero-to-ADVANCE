''' Importing in python is the process of loading a code from a python module into the
    current script. This allows to use the 'functions' and 'variables' defined in the module 
    in your current script as well as any additional modules that the imported module may depend'''

# importing the module
import math
print(math.sqrt(15))
print(math.floor(3.1223231234))
print(math.factorial(5))

# importing the functions or variables directly 
# this is the best approach of importing as it imports only specific functions or variables
from math import sqrt , pi
print(sqrt(9))
print(pi)


# importing everything from the module
from math import *
# Note : This is not the recommended approach


# importing by writing 'as'
import math as m
print(m.sqrt(9))

# specific importing with 'as'
from math import sqrt  as s , floor as f
print(s(4.0))
print(f(3.56745))


# 'dir' function : used to see all the 'functions' and 'variables' present in the module
import math
print(dir(math))


# importing a 'self created module'
import ash_import as a
a.Welcome()      # calling a function from the module
print(a.name)    # calling a variable