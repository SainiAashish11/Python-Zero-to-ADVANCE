# function : It is a block of code which performs the specific task whenever it is called in the program


def Greater_Lesser(a , b):    # 'def' keyword for starting the function 'Greater_Lesser' is the function name
    if(a > b):
        print(f"{a} is greater than {b}")

    elif(a<b):
        print(f"{b} is greater than {a}")

    else:
        print("Numbers are equal")

''' assigning values to arguments before function calling '''
a = 5
b = 10 
c = 9
d = 2
e = 1
f = 1
Greater_Lesser(a , b )  # function calling with arguements/parameters defined inside the function call only
Greater_Lesser(c , d )  # 'c' and 'd' are already defined before function call otherwise will show 'unexpected argument' error
Greater_Lesser(e , f )  # 'e' and 'f' are already defined before function call
 

# Geometric mean

def Gmean(x , y):      # function parameters should be 'variables' not 'literal/defined values'
    gmean = (x * y) / (x + y)
    print(gmean)

Gmean(a  , b )           # function calling
Gmean(c  , d )
Gmean(e  , f )


# string parameters

def name(fname , lname):
    print(f"Hello {fname} {lname}")  # using arguements/parameters in 'print' statement

name("Aashish" , "saini" )


''' 
There are 2 types of functions:
 1- Built-in     : already built in the pyhton library and no need to use 'def'
 2- user defined : user is creating the function as per the need using 'def'keyword 
'''


# concept of pass
def average(a , b):
    pass              # this function is passed and will be taken care in future when it completes

