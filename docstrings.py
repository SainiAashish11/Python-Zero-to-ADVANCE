# docstring : It is the string used to document(working ) the code
# It is written just above the function definition

def square(n):
    '''This function takes the number and provide the square of that number'''

    print(n**2)

square(5)

print(square.__doc__)    # this '.__doc__' attribute provides the docstring of the program

# Difference between 'comment' and 'docstring'
# Comment : It is also a string but ignored by the interpreter
# docstring : This string is not ignored by the interpreter if written just above the function definition

def average(n , m , p):
    print(n , m, p)
    ''' this function is for finding out the average of given numbers'''       # it is a 'docstring'

    print("Average of the numbers is : " , (n+m+p)/3)

average(2,5,6)

print(average.__doc__) 

# Note : When something comes before the docstring it will return 'none' not the 'docstring' written

# PEP 8 : It means 'Python Enhancement Proposal'
# It is the document which when accessed tells 'how to maintain the readibility and scalability of program

import this               # Use to open the document written by  'Tim Peters'
import antigravity        # opens up the 'XKCD comic' 
import __hello__          # prints ' Hello world! '