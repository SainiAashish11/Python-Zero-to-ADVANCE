# parameters : variables or values passed in the function definition
# arguments  : variables or values passed in the function call

""" function arguments are of 4 types:
# 1- Default arguments
# 2- keyword arguments
# 3- Required arguments : They can be positional or keyword arguments
# 4- Variable length arguments 
# 5- positional arguments """

'''Defualt arguments : We can pass the default value while creating the function.
when function calls happen , same 'default value' will be taken by function call'''

def Average(a=2 , b=3):         # parameters have initial values hence they are 'default parameters' | parameters passed in function definition must have 'variable names'
    
    print("the average of two numbers is :" , (a+b)/2)

Average()                       # no values are passed here hence 'default' values will be taken from function definition
Average(4)                      # now value of 'a' will be changed and 'b' value will be taken as 'default' from function definition
Average(b=9)                    # 'b' is overridden here and 'a' will be taken as 'default' value from function definition
Average(b=6,a=10)               # ( keyword arguments ) argument values are provided in cross order hence order does't matter in default arguments and hence 'b' and 'a' values will be exchanged as per the names only



##########################
'''keyword arguments : We can pass the argument (as a 'keyword') and it's value in the function definition only 
and hence order doesn't matter when function calling happens'''


def greet(name, greeting="Hello"):              
    print(greeting + ", " + name + "!")

# Using keyword arguments : explicitely providing 'argument name' and it's value in function call

greet(name="Alice", greeting="Hi")              # here arguments are in same order as in function definition
greet(greeting="Welcome", name="Bob")           # here order of arguments are changed and they will be judged by their names only as 'greeting' arguement is written at first place and 'name' at second specifically



##########################
'''Required arguments : It is necessary to provide their values when there is function call '''

def name(fname , mname , lname = "saini"):      # 'fname' and 'mname' are 'Required arguments' and 'lname' is 'default argument' as value is provided in function definition only
    print("hello"  , fname , mname , lname)

name('Aashish' , '')                            # 'lname' is taking 'default value' and 'fname' and 'lname' are 'required arguments' as their values has to be passed specifically in function call and will go 'positionally' to function parameters
name(fname = 'Aashish' , mname = '')            # 'fname' and 'mname' are passed with their names and 'lname' taken from default value
name(mname = '' , fname = 'Aashish')            # orders of 'fname' and 'mname' are swapped but still they will be judged with their names



#########################
'''Positional Arguments : They are matched to the function parameters based on their order'''

def describe_pet( animal_type , pet_name):
    print(f"I have {animal_type} named {pet_name}")

describe_pet('dog' , 'Loyality')



##########################
'''variable length arguments : when we don't need to mention the number of arguments and their values'''

''' *args (Arbitrary Positional Arguments): This syntax allows a function to accept any number of positional arguments. 
These arguments are collected into a tuple.
'''

''' **kwargs (Arbitrary Keyword Arguments): This syntax allows a function to accept any number of keyword arguments.
These arguments are collected into a dictionary.
'''

# Positional arguments(*)
def sum(*numbers): # using '*' means we are creating a 'tuple' of positional arguments as 'numbers'
    Sum = 0
    for i in numbers:
        Sum = Sum + i
    print("sum of the numbers are : " , Sum)

sum(2,3,4,5,6,7,8,9)                                   # these numbers are pass into the function parameter 'numbers' only once as a single 'tuple'

# keyword arguments(**)
def build_profile(**user_info):
    print(user_info)

build_profile(fname = 'Aashish',                       # we are providing keyword arguments(fname , lname , location , field)
             lname = 'Saini',
             location='princeton',
             field='physics')







