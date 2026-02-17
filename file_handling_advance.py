''' 
    Types of Data for I/O :
      - Text - '12345' as a sequence of unicode chars
      - Binary - 12345 as a sequence of bytes of its binary equivalent
      
    Types of files to deal with : 
      - Text Files : All program files are text files
      - Binary Files : images , videos , music , exe files , etc 
'''

''' 
    How file I/O is done :
    Step -1- Open a file
    Step -2- Read/Write
    Step -3- Close the file
'''

# Writing to a file
# Case 1 - If file is not present then open a file in 'write' mode
f = open('sample.txt' , 'w')
f.write("Hello, This is a new file that i've created with 'write' mode")
f.close()              # file is closed now so can't write until it's not opened again
f.write(" Hello ")     # ValueError: I/O operation on closed file.

#  multiple strings writing to a file ( time consuming way rather use 'list' method )
f = open("sample1.txt" , 'w')
f.write(" This is the first line ")      # using 'f.write()' multiple times for writing
f.write(" \nThis is the second line ")
f.close()

# Case 2 - if file is already present : Old content of the file will be removed and new content will be added
f = open("sample.txt" , 'w')
f.write(" New line added to already existing file ")
f.close()
# Note : if file is not in same directory then provide the complete path of the file


''' how open() works : python loads the file from hard disk to RAM in buffer memory and then parse it completely and after writing it again release the file to the hard disk again '''


# append mode 'a'
# problem with 'w' mode : write mode replaces the already present content in the file with new content
# use append mode to write without replacing
f = open('sample.txt' , 'a')   # 'a' is append mode
f.write('\nI am Fine now')
f.close()


# write multiple strings using 'list' data type : this method will remove the old content with new content
l = [ 'Hello\n' , 'I hope you are doing well\n' , 'So how is your mother now\n' , 'i hope she is doing well' ]
f = open('sample.txt' , 'w')
f.writelines(l)
f.close()

'''
Note : f.close() for 2 reasons : 
        1- memory should not be used without any reason
        2- anyone can access the file from the buffer memory once system is hacked
'''

# --------------------------------------------------------------------------------------------#
# reading from files using read()
f = open('sample.txt' , 'r')
s = f.read()
print(s)
f.close()

# reading upto 'n' characters
f = open('sample.txt' , 'r')
s = f.read(10)                # number of characters inside read() function
print(s)
f.close()

# readline() : to read line by line
f = open('sample1.txt' , 'r')
print(f.readline() , end = '') 
print(f.readline() , end ='' )
f.close()
# Note : readline() and print() functions change lines after the execution hence we need to use 'end' operator for no gaps
# Note : readline() : Use it when there is big file and we don't want to load such a big file into the memory 

''' -------------------------------------------------------------------------------------------------------------------------------------- '''
# using Context Manager ( with ) : 'with' keyword closes the file as soon as the usage is over
# writing using 'with' operator, old content of the file removed by new content
with open('sample1.txt' , 'w') as f:
    f.write('This is the third line')

# 'read' using with keyword
with open('sample1.txt' , 'r') as f:
    print(f.read())           # we can also use 'readline' here

# moving within a file -> 10 char then 10 char
with open('sample1.txt' , 'r') as f:
    print(f.read(10))         # 10 characters will be printed and then 'print()' function will take to next line
    print(f.read(10))         # next 10 characters will be printed
''' here buffer memory keeps the count so that it can tell where you're right now in 'read' mode '''



# benefit of reading chars by chars -> to load a big file in memory

# Creating a big data file
''' Best way to load big files in chunks of data '''
big_L = ["Hello World\n" for i in range(1000)]
with open('big.txt' , 'w') as f:
    f.writelines(big_L)  

# Loading the 'big.txt' in chunks
with open('big.txt' , 'r') as f:
    chunk_size = 100
    while len(f.read(chunk_size)) > 0:   # checking till when the 'length of f.read()' is > 0
        print(f.read(chunk_size))        # printing 100 characters
        f.read(chunk_size)               # loading the next chunk_size character from the file if exists


#----------------------------------------------------------------------------------------------#
# seek : it positions the buffer memory at the given location as parameter
# tell : it tells the location of the buffer memory position
with open('sample.txt' , 'r') as f:
    print(f.read(10))       # starting from 1-10
    print(f.tell())         # tells where the buffer memory position is
    f.seek(0)               # it again position the buffer memory at given parameter position i.e. 0 ( start )
    print(f.read(10))
    print(f.tell())
    f.seek(15)              # positions at 15
    print(f.read(10))       # now reads from 15 to 25 = 10 characters
    print(f.tell())
    
# seek during 'write' operation in the file
with open('sample.txt' , 'w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('X')            # this operation now remove the 'first place character' and then write 'X' at first place only coz 'seek' points the 'writer' at 'H'
# output : Xello



#----------------------------------------------------------------------------------------------#
'''
Problems with working in text mode
   1- Can't work with binary files like images
   2- not good for other data types like int/float/list/tuples
'''

# working with binary files ( images , videos , music , exe file )
# 'rb' => read binary mode and 'wb' => write binary mode
with open('Italy_coast_sea_houses.jpg' , 'rb') as f:     # opening image in read binary (rb) mode
    with open('Italy_copy.jpg' , 'wb') as wf:            # opening image in write binary (wb) mode to copy the same image
       wf.write(f.read())                                # writing the copied image via f.read()



# working with other data types like int, float , list , tuples , etc
with open('sample.txt' , 'w') as f:
    f.write('5')                                         # 5 is converted to string first the written in the file


# explicit conversion for other data types to be valid inside file operations
with open('sample.txt' , 'r') as f:
    print(int(f.read()) + 5)                             # f.read() content is firstly converted to 'int' first then '5' is added to the content


# dictionary
d = {
    'name' : 'Aashish',
    'age'  : 24,
    'gender' : 'Male'
}

with open('sample.txt' , 'w') as f:
    f.write(str(d))                      # explicit conversion of 'dictionary' into a 'string'

# Note : Only 'string' data type can be added using f.write() function   


# Note : Whatever data type we'll add to a file, it is only possible to regain that data type with 'Serialization' and 'Deserialization' technique
with open('sample.txt' , 'r') as f:
    print(dict(f.read()))                # ValueError: dictionary update sequence element #0 has length 1; 2 is required


#----------------------------------------------------------------------------------------------#
''' 
    Serialization   : It is the process of converting python data types to JSON format
    Deserialization : It is the process of converting JSON formats to python data types
    - It is a Universal Data format, understandable to all programming languages
    - JSON = Javascript On Notation
'''

# Serialization

# making a list in a JSON file format
L = [ 1 , 2 , 3 , 4 , 5]

import json
with open('demo.json' , 'w') as f:
    json.dump(L , f)      # L is the list and 'f' is the file handler of the JSON module


# making a dictionary in a JSON file format
d = {
    'name' : 'Aashish',
    'age'  : 24,
    'gender' : 'Male'
}

import json
with open('demo.json' , 'w') as f:  
    json.dump(d , f , indent = 4)     # indent = 4 is used for the spacing of the dictionary key-value pairs from the brackets


# Deserialization
import json

with open('demo.json' , 'r') as f:
   d = json.load(f)      # loading the JSON file into 'd' variable
   print(d)
   print(type(d))        # type of the data type will be the same as we've used during serialization


# Serialize and Deserialize a tuple : It creates 'tuple' as 'List' only in the file
import json

t = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10)
with open('demo.json' , 'w') as f:
    json.dump(t , f)

with open('demo.json' , 'r') as f:    # reading the file
    d = json.load(f)
    print(d)
    print(type(d))                    


'''  Serializing and Deserializing Custom Objects ( class ) '''
# making a custom object ( class )
class Person:
    def __init__( self , fname , lname , age , gender ):
         self.fname  = fname
         self.lname  = lname
         self.age    = age
         self.gender = gender

person = Person('Aashish' , 'Saini' , 24 , 'Male')    # 'person' is the object of 'Person' class

import json

def show_object(person):
    if isinstance(person , Person):
        return "{} {} age -> {} gender -> {}".format(person.fname , person.lname , person.age , person.gender)

with open('demo.json' , 'w') as f:
     json.dump(person , f , default = show_object)



# Custom object conversion into Dictionary data type form
class Person:
    def __init__( self , fname , lname , age , gender ):
         self.fname  = fname
         self.lname  = lname
         self.age    = age
         self.gender = gender

person = Person('Aashish' , 'Saini' , 24 , 'Male')    # initializing 'person' object of 'Person' class with Arguments


import json

def show_object(person):                # function which will tell that if the 'object' is of Person class then show output written in 'return' operator
    if isinstance(person , Person):     # checking that 'person' is the instance of 'Person' class or not
        return {'name' : person.fname + ' ' + person.lname , 'age' : person.age , 'gender' : person.gender}

with open('demo.json' , 'w') as f:
     json.dump(person , f , default = show_object , indent = 4)     # ' default' is the keyword for calling 'show_object' function for showing it's details


''' Deserialising the custom object '''
import json
with open('demo.json' , 'r') as f:
    print(json.load(f))


#-------------------------------------------------------------------------------------------------------3

''' 
    Pickling : process whereby Python object hierarchy is converted into a byte stream, and unpickling is the
               inverse operation, whereby a byte stream(from a bianry file or bytes-like object) is converted back
               into an object hierarchy 
'''

class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age  = age

    def display_info(self):
        print("Hi my name is" , self.name, "and I am" , self.age , "year old")
    
p = Person("Aashish" , 24)   # 'p' is object of class Person

# writing 'p' object in binary file
import pickle                         # making 'p' object in binary form
with open('demo.json' , 'wb') as f:
    pickle.dump(p , f)

# Reading 'p' object as binary file
import pickle
with open('demo.json' , 'rb') as f:   # reading the binary 'p' object
    p = pickle.load(f)
p.display_info()              # calling the 'display_info()' function from the class


''' 
Note: 
    DIfference in Pickle vs JSON 
    - Pickle lets the user to stroe data in binary format ( when machine learning models has to run on other machines )
    - JSON lets the user to store data in human readable format ( key-value pairs )
'''