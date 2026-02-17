'''
    Map , Filter and Reduce are the built-in python functions which applied on a sequence of elements and return a new sequence.
    These functions are known as higher order functions, as they take other functions as their arguments
'''

# Map : Map function apply given argument function to each element in a sequence and returns a new sequence
#       with transformed elements
# Syntax : map( function , iterable )
# 'iterable' can be a list, tuple, or any other iterable object

def cube(num):
    return num * num * num
    
l = [1 , 2 , 3 , 4]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)


# alternate way to perform above task on a list :
def cube(num):                       # cube function for calculating the cube of the number 'num'
    return num * num * num

l = [1 , 2 , 3 , 4]
newl = list(map(cube , l))     # 'cube' is the function and 'l' is the iterable as arguments in 'map' function
print(newl)


# using lambda function inside map function
l = [1 , 2 , 3 , 4]
lst = list(map(lambda x: x*x*x , l))     # 'map' function points/locates the 'lambda cube function' on each element of the list 'l'
print(lst)

# ---------------------------------------------------------------------------------------------------------#

# filter : filters the sequence of elements as boolean values, which qualify the given conditions
# Syntax : filter( function, iterable )

def filter_function(a):
    return a > 4

l = [1 , 20 , 3 , 4 , 8 , 10 , 50]
new_list = list(filter(filter_function , l))    # calling 'filter_function' as argument insdie 'filter' built-in function
print(new_list)


# using lambda function inside filter function
l = [1 , 20 , 3 , 4 , 8 , 10 , 50]
lst = list(filter(lambda x: x > 2 , l))    # lambda function for values greater than 2
print(lst)

# ----------------------------------------------------------------------------------------------------------#

# Reduce : This function reduces the sequence of elements using the given operation on them
# It needs to be import from 'functools' module

# Example
from functools import reduce                # importing the 'reduce function from the 'functools' module

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7]

def Sum(x , y):       # function for sum of numbers
    return (x+y)

Answer = reduce(Sum , numbers)
print(Answer)

# Working : 'x' and 'y' variables are pointing to consecutive numbers in the 'numbers' list 
#           and (x + y) making the sum of the elements in the list and 'reduce' function 
#           making the 'numbers' list shorter till last element is not summed            