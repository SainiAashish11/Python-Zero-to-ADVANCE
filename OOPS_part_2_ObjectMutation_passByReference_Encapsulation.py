# The biggest power of the OOP is to create Data type of our own need. 
# For Example : Fraction ( x/y ), e^x , etc


''' Coordinate Geometry Question '''
''' Write OOPS Classes to handle the following scenerios:
    - A user can create and view 2D coordinates
    - A user can find out the distance between 2 coordinates
    - A user can find the distance of a coordinate from origin
    - A user can check if a point lies on a given line
    - A user can find the distance between a given 2D point and a given line
'''
# Class 'Point' initialization
class Point:

    # constructor
    def __init__(self , x , y):
        self.x_cod = x
        self.y_cod = y


    # telling python how to show coordinates
    def __str__(self):
        return '<{},{}>'.format(self.x_cod , self.y_cod)
    

    # creating 'euclidean_distance()' method for distance between 2 points
    def euclidean_dist(self , other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5      # square root = sqrt((x2 - x1)^2 + (y2 - y1)^2))
    

    # dist_from_origin() method
    def dist_from_origin(self):
      # return (self.x_cod**2 + self.y_cod**2)**0.5        # formula based approach
        return self.euclidean_dist(Point(0,0))             # here one point is 'self' as 'object' and other point is initialized inside the method as 'Object instance' - Point(0,0)
    


# Class 'Line' initialization
class Line:

    # constructor
    def __init__(self , A , B , C):
        self.A = A
        self.B = B
        self.C = C


    # __str__ method to show the line format
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A , self.B , self.C)
    

    # method to check 'point lies on the line' or not
    def Point_on_line(line , point):
        if ((line.A * point.x_cod) + (line.B + point.y_cod) + (line.C)) == 0:
            return "Point lies on the line"
        else:
            return "Point does not lie on the line"


    # method to find the distance between a 2D point and a line
    def Dist_btw_point_line(line , point):
        return abs(line.A * point.x_cod + line.B * point.y_cod + line.C) / (line.A**2 + line.B**2)**0.5
        

    # method to find that two lines are intersecting or not
    def intersecting(line1 , line2):
        if line1.A/line2.A != line1.B/line2.B:      # Intersection criteria => (a1/a2 != b1/b2)
            return 'Lines are intersecting'
        else:
            return 'Lines are non-intersecting'


# creating and viewing points
p1 = Point(0 , 0)
p2 = Point(1 , 1)
print(p1)
print(p2)

# calculating the euclidean-distance
print(p1.euclidean_dist(p2))     # self = p1 and other = p2 as arguments in 'euclidean_distance' method

# calculating the distance of point from the origin
p3 = Point(2 , 3)
print(p3.dist_from_origin())     # 'p3' object will go as 'self' inside the method 

# creating a Line-class object
l1 = Line(3 , 4 , 5)
print(l1)

# checking point on line
p4 = Point(2 , 3)                 # creating a new point object
l2 = Line(2 , 3 , 6)              # creating a new line object
print(l1.Point_on_line(p4))       # 'l1' line object will go as 'self' and 'p4' will go as 'other' in method

# calculating the shortest distance of a point from a line
p5 = Point(3 , 4)
l3 = Line(4 , 6 , 8)
print(l3.Dist_btw_point_line(p5))

# lines are intersecting or not
print(l2.intersecting(l3))

''' Note : Classes are calling each other's variables and methods becasue both the classes are in the same file.
           Otherwise we have to import the other class file into our class code first 
'''

# -------------------------------------------------------------------------------------------------------------------#

''' Attribute Creation from Outside of the Class '''
class Person:
    def __init__(self , name , country):
        self.name = name 
        self.country = country

    def greet(self):
        if self.country == "India":
            return f'Namaste {self.name}'
        
        else:
            return f'Hello {self.name}'
        
p = Person("Aashish" , "India")
print(p.greet()) 

# creating attribute (variable) from outside
p.gender = "Male"
print(p.gender)

# ------------------------------------------------------------------------------------------------------------------#

''' Reference Variables : 
1- Holds the object's memory address not the original object
2- We can create objects without reference variable as well
3- An object can have multiple reference variables
4- Assigning a new reference variable to an existing object does not create a new object '''

class Person:
    def __init__(self):
        self.name = 'Aashish'
        self.gender = 'Male'

p = Person()    # 'p' is reference variable which stores the memory address of the class object
q = p           # 'referencing of varaibles' where 'p' and 'q' both are pointing towards the same memory address 

print(id(p))
print(id(q) , '\n')

print(p.name)
print(q.name , '\n')

# shadowing of the attribute
q.name = 'Saini'                         # changing the values of data variables outside the class
print(q.name)
print(p.name , '\n')

# ------------------------------------------------------------------------------------------------------------------#

''' Pass By reference : when Object's address is sent to function as argument '''
class Person:
    
    # constructor
    def __init__(self , name , gender):
        self.name = name
        self.gender = gender

# function coz made outside the class
def greet(person):                           # 'person' object passed inside the function as 'argument'
    print('Hi, My name is ', person.name, 'and I am a' , person.gender)    # accessing the attributes of 'person' object i.e. 'person.name' and 'person.gender'
    print(id(person))                        # checking whether the memory addresses of 'p' object and 'person' are same or not,if 'yes' then means 'pass by reference'
    print(person.name)
    # returning an object inside function
    p1 = Person("Saini" , "Male")
    return p1


# initilaizing the object of class 'Person' and callin greet() function without capturing the returned 'p1' object
p = Person("Aashish" , "Male")
print(id(p))                    # same memory address as the 'person' in the greet() function
greet(p)                        # we are not capturing the returned 'p1' from greet() function as 'x = greet(p)'
p.name = "Ankit"                # changing the 'name' attribute after greet() function call will change the 'name' in the memory address

# capturing the returned object 'p1' from 'greet()' function after executing the print() statement
x = greet(p)
print(x.name)        # 'x.name' is now changed from 'p.name'
print(x.gender)      # 'x.gender' is now changed from 'p.gender'

''' Note : If any attribute ( name / gender ) will be changed by 'p' or 'person' then it will reflect the change for both the objects coz both are pointing to same memory location '''


#---------------------------------------------------------------------------------------------------------------------#

''' Object Ki Mutability '''
class Person:

    def __init__(self , name , gender):
        self.name = name
        self.gender = gender

def greet(person):
    person.name = 'Ankit'          # 'name' attribute changed using 'person' object but still 'p' object is also pointing to this location as well
    print(person.name)
    return person                  # changed 'person' object now returned to greet() function


p = Person('Aashish' , 'Male')
print(id(p))                            # execution step-1
print(p.name)                           # execution step-2
p1 = greet(p)                           # execution step-3 => capturing the returned 'person' object from greet() function
print(id(p1))                           # execution step-4 => printing memory address of changed 'object' ( object changed in greet() function ! please see above )

# Here the 'name' attribute changed using 'person' object but 'p' and 'p1' also pointing to same location hence they can see the changes which means
# 'Objects' in Python are Mutable data types that's why the memory address of the 'modified object'( person.name = "Ankit") is not changed here

# ----------------------------------------------------------------------------------------------------------------------#

''' Encapsulation : Data + Getter() and Setter() => these 3 things ( Data and methods ) are binded like a medicine in the capsule '''
''' Definition : Encapsulation means wrapping up data (variables/attributes) and methods (functions) into a single unit → the class.
                => It also means restricting direct access to some variables/methods to protect the object's internal state.'''

# Always make your class variables private using double underscore => '__VariableName'
# Always make getter() and setter() for the private attributes to access the attributes from the outside of the class with your own 'protected conditions'
# Instance variable : Special Variable which have different values for different Objects

class Person:

    def __init__(self , name):
        self.__name = name                 # private attribute '__name' using '__' double underscore

    def get_name(self):
        return self.__name     
    
    def set_name(self , new_name):
        if isinstance(new_name , str):     # here 'new_name = Saini' is not only a string but an instance of class i.e. 'name' attribute so 'isinstance()' function was required to check the string type here
            self.__name = new_name         # changing old name with new_name
            return self.__name
        else:
            return f'Bhak Sale ! Galat Type Daalta Hai'


# creating object of class 'Person'
p = Person("Aashish")
print(p._Person__name)       # attribute changed to '_Person__name' variable in the memory


# using getter() method to see what's inside 'name' attribute
print(p.get_name())


# using setter() method to change the 'name' attribute from outside
print(p.set_name("Saini"))

''' 
Note : What “private” means here (name mangling)

    - Writing 'self.__name' inside Person class becomes '_Person__name' in the instance.

    - That's why 'p.__name' would fail, but 'p._Person__name' works.

 Goal: prevent accidental access and subclass collisions, not absolute hiding.
'''

# ----------------------------------------------------------------------------------------------------------------------#

''' Collection Of Objects '''
class Person:

    def __init__(self , name , gender):
        self.name   = name
        self.gender = gender

p1 = Person("Aashish" , "Male")
p2 = Person("Saini" , "Male")
p3 = Person("Arunima" , "Female")


# Creating a list of these p1,p2 and p3 objects
L = [p1 , p2 , p3]
# print(L)                            # prints the memory addresses of the objects coz '__str__' function is not present to tell how to print the class objects

# access of objects via for-loop
for i in L:
    print(i.name , i.gender)          # 'i' points to the memory location of object and hence can access the attributes


# storing objects in a 'Set' is possible beacuse both the objects 'p1' and 'p2' are different and have different memory addresses so can be hashed (__hash__) by the python
S = {p1 , p2 , p3}
print(S)


# storing objects in a dictionary
d = {'p1':p1 , 'p2':p2 , 'p3':p3}
 
for i in d:                 
    print(i)          # print keys only

for i in d:         
    print(d[i])       # print the values => objects

for i in d:           # print the attribute values of the objects
    print(d[i].name , d[i].gender)


# -----------------------------------------------------------------------------------------------------------------------#

''' Static variables ( vs Instance variables )'''

# Static Variable   : It is the 'Class' variable whose value remains same for every Object of the class
# These can be Declared above the constructor and can be accessed using class name as 'Class.variable_name'
# Example : IFSC code of the Bank , Bank Address , College Name , etc

# Instance Variable : It is the 'Objcet' variable whose value is different for each Object
# Declared inside the constructor and can be accessed using object name as 'Object.variable_name'
# Examples : name of the customer , customer Bank Balance , Student CGPA , etc

class Person:
    
    # Private static variable
    __counter = 1


    # utility functions which can be accessed without objects of the class coz we are not providing any 'self' parameter to the function
    @staticmethod
    def get_counter():               # method without any argument is accessed using 'class-name'
        return Person.__counter      # returning the '__counter' variable using 'Person' class


    def __init__(self , name):
        self.name = name
        self.cid = Person.__counter                # accessing 'static variable' using 'Person' class name
        Person.__counter = Person.__counter + 1    # incrementing 'counter' variable


c1 = Person("Aashish")
c2 = Person("Saini")
c3 = Person("Arunima")

# printing the customer ids
print(c1.cid)
print(c2.cid)
print(c3.cid)

print(Person.get_counter())
print(id(Person._Person__counter))       # getting the memory address of '__counter' static variable using class name and mangled name(name changed after making it private variable) in the memory
    


