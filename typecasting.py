# typecasting : conversion of one data type to another 
# some in-built typecasting functions in python are int(), float(), str(), bool(), ord() -> ASCII values , hex(), oct(), set(), list(), tuple(), dict(), etc
# explicit Typecasting - coversion of data type done by the developer

# Note : 'int , float and bool' are not convertible to -> list() , tuple() , set() -> but convertible to each other 
# Note : 'string' is convertible to list() , tuple() , set() and vice-versa


# String values
a = "1"
b = "2"

print( a + b )                    # it is concatenating the strings as it is : 12
print( int(a) + int(b) )          # here , int() function converts the valid string data into an integer and then adding them as -> 1 + 2 = 3
print( float(a) + float(b) )      # here , float() function converts the valid string data into float values and adds them as    -> 1.0 + 2.0 = 3.0
print(list(a) + list(b))          # 'strings' are iterable hence 'list' is created


# Integer values
a = 1
b = 2

print( str(a) + str(b) )          # here , str() function converts the integer data type into string and then concatenating them as 12
print( a + b )                    # simple adding of integers are taking place
print( bool(a) + bool(b))         # bool() function converting the value a=1 and b=2 as 1 (true) and hence -> True + True = True
print(list([a] + [b]))            # as 'a' and 'b' are integers so can't direct put in the 'list' due to non-iterable elements so they are manually wrapped inside the 'list' here


# Float values
a = 1.1
b = 2.9

print( str(a) + str(b) )
print( int(a) + int(b) )                 # 'float' to 'int' conversion will always performed on integers before decimal
print( int(a) - int(b) )                       
print(list([a]) + list([b]))             # manual wrapping of float values in the list


# list of 'string' values is converted into 'numeric' entries in the list
data = [ '100' , '200' , '300' ]
num_data = [ int(x) for x in data]
print(num_data)


# implicit Typecasting - conversion done by the interpreter itself not by developer
a = 1
b = 2.5
print( a + b)    # here 'a' is converted to 'float' data type by the python interpreter itself



a = ('a' , 1)
b = ('b' , 2)
print(dict([a]) | dict([b]))
print(dict((a,)))                     # (a,) is treated as tuple now
# [a] -> list of tuple will be converted to 'key-value' pair -> {'a' : 1}
# |   -> is used to merge two dictionary items at one place  -> {'a': 1} | {'b': 2}
''' 
- dict() needs an iterable of 2-element iterables.
- A single tuple like ('a', 1) is not in the correct form
- But wrapping it inside a list ([('a', 1)]) creates a valid iterable of key-value pairs.
'''
''' 🚀Bonus Tip
If the keys overlapped, the right dictionary wins:
{'a': 1} | {'a': 99}  → {'a': 99}
'''
