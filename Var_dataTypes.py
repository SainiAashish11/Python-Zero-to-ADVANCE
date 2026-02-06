# variables and data types
# variables are used to store the different data types 
# all data types are built-in 'classes' in python as per its 'object-oriented paradigm'

a = 1                    # it is an "int" data type and 'a' is the object of class'int'
print(a)
print(type(a))           # type() function specifies the data type of the variable i.e. 'a'
print(type(a).__name__)  # 'type().__name__' tells the exact data type 

b = "Aashish"       # it is a "string" data type and 'b' is the object of class'str'
print(b)
print(type(b))


c = True            # it is a "boolean" data type and 'c' is the object of class'bool'
print(c)
print(type(c))  

d = None            # it is a "none" data type where 'none' is data type means it holds 'no value' and 'd' is the object of class'NoneType'
print(d)
print(type(d))

e = 5+2j            # it is "complex" data type 
print(e)
print(type(e))

# ordered means whenever print statement is executed 'output' will remain same as how you entered your values in the object

# list : ordered data type
list = [ 8, 5, 6, [4,3], ["apples", "bapples"]]                  # list is an ordered collection of different data types within a square bracket and are mutable means can modified after creation
print(list)                         
print(hex(id(list)))                                             # getting the 'list' memory address and changing it into the hexadecimal number which is the memory location of the heap memory
list.append(9)                                                   # using "list.append()" we are adding the number at the 'end' of the 'list'
print(list)
print(hex(id(list)))                                             # memory location still remains same even after the modification(.append() function) into the 'list' items



# tuple : ordered data type
tuple = (("parrot", "sparrow"), "cow", a, b, c, d, 1 )           # tuple is an ordered collection of different data types but are immutable and cannot be modified after the creation but can be defined again with the same name and different entries
print(tuple)


# dict : ordered data type
dict = { "name" : "aashish" , "age" : 21 , "CanVote" : True }    # dict is a dictionary which is an ordered collection of data containing a 'key-value' pairs called 'mapped-data' and is 'immutable' 
print(dict)


# set : unordered data type
set = { 1 , 2 , 3 }
print(set)
print(hex(id(set)))        # checking the hexadecimal address of "set" object

set.add(4)
print(set)
print(hex(id(set)))        # checking the hexadecimal address of the "updated set" as 4 is now added to it


# mutable type   - when an object is created with some values inside, we can change the object values in future as per the requirement but address will remain same for the data variable
# immutable type - when object values cannot be changed in future and has 'hash' value
# 'ordered' means output will be in same 'order' as in the input while in 'unordered' output will 'not have any order'
# list[] , set{} , dict                                         -> mutable data types 
# int , float , string , tuple() , frozenset , dict(keys), bool -> immutable data types but can be rebinded(assigned) to new value/object during the program

'''
- Hashing : providing the unique memory address or space to immutable object
Hashable Objects are Immutable: An object can only be "hashable" if its 'hash' value never changes during its lifetime.

Why? If an object's contents could change after its 'hash' value was calculated and used (e.g., as a dictionary key), 
then its 'hash' value would become invalid. If you later tried to look up that 'key', Python would calculate a different 
'hash' value and would likely not find the original entry, leading to errors or corrupted data.

Therefore:
Immutable types -> int, float, str, tuple, frozenset, bytes/bool are hashable. You can use them as 'dictionary keys' and 'Frozen-set elements'.

Mutable types   -> list, dict, set are not hashable. You cannot use them directly as 'dictionary keys' or as 'elements within a 'Frozen-set'.

'''
