''' Identifiers : name of variable , function or class '''

''' Namespaces : A namespace is a space that holds names(identifiers) and their values.
                Programmatically speaking, namespaces are dictionary of identifiers(keys) 
                and their objects(values)'''

''' Types of Namespaces :
    1- Builtin Namespace
    2- Global Namespace
    3- Enclosing Namespace
    4- Local Namespace 
'''

''' Scope : Place where the 'namespace' is directly accessible '''

''' LEGB(Local => Enclosing => Global => Built-in) rule : The interpreter searches a name from inside out, looking in the local => enclosing => global => built-in scope.
        If the interpreter doesn't find the name in any of these locations, then python raises a 'NameError exception'
'''

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

'''Local scope   → variables declared inside a function (exist only within that function).
   Global scope  → variables declared outside any function (exist everywhere in the program).
'''

# Example-1: Local and Global variables
a = 2                         # 'a' is in global scope hence global variable

def temp():
    b = 3                     # 'b' is in the local scope of function 'temp()' hence local variable
    print(b)

temp()      # executing withing local scope
print(a)    # executing within global scope


# Example-2: local and global variables with same name
a = 3           # global 'a'

def temp():
    a = 4       # local 'a'
    print(a)

temp()         # executing within local scope 
print(a)       # executing within global scope


# Example-3: local variable doesn't exist but global does then interpreter searches as per the LEGB rule
a = 3

def temp():
    print(a)

temp()         # executing within global scope 
print(a)       # executing within gloabl scope


# Example-4: trying to change the value of global variable within local scope ( this code will show 'UnboundLocalError' )
a = 3

def temp():
    a += 1       # trying to change the gloabl variable 'a'
    print(a)

temp()         
print(a) 

# Example-5: changing global variable in local scope using 'global' keyword
a = 3

def temp():
    global a
    a += 1
    print(a)

temp()        # trigger the 'temp()' function where value of global 'a' is accessible using 'global' keyword 
print(a)      # now printing the changed value of global 'a'


# Example-6 : creating a global variable within local scope

def temp():
    global a     # triggering 'a' as global variable 
    a = 10       # initializing value to 'a'
    print(a)

temp()        # it triggers the 'temp()' function and then 'a' variable is initialized in it as 'global' variable
print(a)      # printing 'a' as global variable


# when function has local parameter 'z'
def temp(z):
    print(z)

a = 4         # global variable
temp(5)       # giving '5' in temp() as local parameter
print(a)
print(z)      # 'z' can't be accessed from global scope hence will show 'NameError'

# -------------------------------------------------------------------------------------------------------------------------------------------- #

''' Built-in scope : Everything available in the python library when we start writing the code in python
Ex : print() function , len() function , Errors , Exceptions , etc
'''

# checking what things are present inside the built-in scope
import builtins
print(dir(builtins))

# renaiming built-ins
L = [1 , 2 , 3]
print(max(L))        # this max() built-in function works properly and gives the max value from the list 'L'

def max():
    print('Hello')

max(L)     # this max() will throw error due to passing the un-wanted argument 'L' which is not passed in the function definition

# --------------------------------------------------------------------------------------------------------------------------------------------- #

''' Enclosing Scope : When an scope exists inside the already existing scope (function within the function)'''
''' Enclosing can have many number of functions inside it and can have 'Enclosing scope 1 => Enclosing scope 2 => Enclosing scope 3 => and so on......'''
def outer():
    a = 3           # enclosing scope 'a'
    def inner():
        a = 4       # local scope 'a'
        print("Inner/local scope function : " , a) 
    inner() 
    print("Outer/Enclosing scope Function : " , a)

a = 1       # global scope 'a'
outer()
print("Main/global scope Program is running : " , a)

# non-local keyword for changes
def outer():
    a = 1          # enclosing scope variable
    def inner():
        nonlocal a                # 'nonlocal' keyword for accessing the value of 'non-local' scope variables i.e. enclosing scope
        a += 1                    # changing non-local 'a' variable
        print("inner : " , a)
    inner()                       # calling local function - inner()
    print("outer : " , a)

a = 3              # global scope variable
outer()
print("Main program : " , a)

# --------------------------------------------------------------------------------------------------------------------------------------------- #

''' Decorators : A decorator in python is a function that receives another function as input and adds some functionality(decoration) to it 
                 and returns it.
~ In Simple Analogy : Baap ke marne ke baad bhi Bachhe unki property use kar sakte hai

~ This can happen only because python functions are 1st class citizens means you can do any opertation on them 
i.e. => add, remove , print , pass to function , passing into list/set/tuple/dictionary as thier objects) , etc

~ There are 2 types of decorators available in python :
1- Built-in decorators     : Examples - @staticmethod , @classmethod , @abstractmethod , @property , etc
2- User defined decorators : we can create them as per our needs
'''

# ------------------------------------------------------------------ #
# Example - Closure concept in python : child function(wrapper() here) can access the variables/functions of the parent function(my_decorator() here) even after it is executed and vanishes from the memory
def my_decorator(func):                # function 1 as decorator
    def wrapper():                     # function 2 as wrapper
        print('*******************')
        func()                         # function 3 which is passed as an argument in 'decorator'
        print('*******************')
        
    return wrapper         # returning the 'wrapper()' function to 'my_decorator()' function


def display():                # function 3 as 'func' which passed as an argument in 'my_decorator()'
    print('Hello Aashish')

a = my_decorator(display)     # taking the returned function wrapper() in variable 'a'
a()                           # calling 'a' function which is wrapper() function only now

# ------------------------------------------------------------------ #
# Example - Better syntax for above question
def my_decorator(func):
    def wrapper():
        print('***************')
        func()
        print('***************')

    return wrapper


@my_decorator         # applying the 'my_decorator' function on 'display()' function
def display():
    print('Hello Aashish')

display()     # calling 'display()' function only now
 

# ----------------------------------------------------------------- #
# Example - Generic decorator which handles any number of arguments
import time    # importing 'time' module to use time functionalities

def timer(func):
    def wrapper(*args):          # '*args' is a tuple of arguments and is used to give any number of arguments to the 'wrapper()' function
        start = time.time()      # time.time() function tells the current time
        func(*args)
        print('time taken by : ' , func.__name__ , 'is' , time.time() - start , 'seconds')        # 'func.__name__' prints the actual name of the function 

    return wrapper       # returning 'wrapper()' function to the 'timer()' function above


# function 1
@timer                      # giving 'display' function to 'timer()' decorator by using '@timer'    
def display():
    time.sleep(1)           # time.sleep() waits for given seconds to run the further code 
    print('Hello Aashish')

# function 2 with one parameter
@timer
def square(num):
    time.sleep(1)
    print(num**2)

# function 3 with two parameters
@timer
def power(a , b):
    time.sleep(1)
    print(a**b)


# function calling with valid arguments
display()
square(3)
power(2 , 3)


# ---------------------------------------------------------------- #
# Example - Decorator with parameters
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError('Not a Valid Data type')
        return inner_wrapper
    return outer_wrapper


# function-1 with 'integer' parameter check 
@sanity_check(int)
def square(num):
    print(num**2)

# function-2 with 'string' parameter check
@sanity_check(str)
def greet(name):
    print('Hello ' , name)


# function calling
square(2)
greet('Aashish')