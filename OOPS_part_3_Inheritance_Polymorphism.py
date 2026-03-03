''' Class relationships 
    - Aggregation
    - Inheritance
'''

# Aggregation ( has a relationship ): One class owns the other class ( owner and property )
# Examples : Customer( class1 ) has a Address( class 2 ) , Restaurant( class 1) has a Menu( class 2 )
# Code:
class Customer:

    def __init__(self , name , gender , address):
        self.name    = name 
        self.gender  = gender
        self.address = address

    def print_address(self):
        return self.address.get_city() , self.address.pin , self.address.state
    
    def edit_profile(self, new_city , new_pin , new_state):                # method for changing the address of the customer
        self.address.edit_address(new_city , new_pin , new_state)          # 'self' is calling the 'edit_address()' function from 'Address' class

    

class Address:
    def __init__(self , city , pin  , state):
        self.__city  = city                           # '__city' is private variable amd can't be accessed in any other class becasue we can't do it without getter() function
        self.pin   = pin 
        self.state = state

    def get_city(self):                # getter() function for fetching the private variable '__city'
        return self.__city
    
    def edit_address(self , new_city , new_pin , new_state):      # 'edit_address()' method with valid parameters
        self.__city  = new_city
        self.pin     = new_pin
        self.state   = new_state

add1 = Address("Gurgaon" , 122011 , "Haryana")
cust = Customer("Aashish" , "Male" , add1)            # 'add1' object of class 'Address' is passed to the constructor of class 'Customer'

print(cust.print_address())

cust.edit_profile("Saharanpur" , 247001 , "UP")     # creating object of 'Customer class' for changing the address of the customer
print(cust.print_address())                         # calling 'print_address()' method using 'cust' object of 'Customer' class

# Note : Main Class( Customer ) cannot access the owned class's( Address ) private attributes(__city)
#         but can be accessed using => ._ClassName__VariableName (name mangling method )

''' 
    (-)  in fornt of variable/method names in class diagram represents the Private variables/methods
    (+) represents the public variables/methods 
'''

# -------------------------------------------------------------------------------------------------------------------------------------------- #

# Inheritance : Jo paap ka hai vo bete ka bhi hai
# Why Inheritance ? => Code resusability 
# Always think about if you can use inheritance in your program coz this will optimise the code
''' What can be accessed from the Parent Class by Child Class
    1- Constructor
    2- Non-Private attributes(variables)
    3- Non-Private Methods
'''

# Example: 
# Parent class
class User:

    def __init__(self):
        self.name = "Aashish"

    def login(self):
        print("login")


# child class
class Student(User):    # writing 'User' in parenthesis will allow 'Student' class to inherit all the properties of the class 'User'

    def enroll(self):
        print("Enroll into the Course")


u = User()            # 'User' class object
s = Student()         # 'Student' class Object

print(s.name)         # accessing 'User' class attribute i.e. 'name' using 'Student' class object i.e. 's'


# -------------------------------------------------------------------------------------------------------------------------------------- #

# child class cannot access private attributs/methods of the parent class
class Phone:

    def __init__(self , price , model_year , brand):
        print("I am inside the Parent class right now")
        self.__price    = price
        self.model_year = model_year
        self.brand      = brand

    def Phone_memory(self , memory):
        self.memory = memory
        return self.memory
    

class SmartPhone(Phone):

    def Details(self):
        print(self.__price)


s = SmartPhone(12000 , 2023 , "Samsung")      # 'SmartPhone' class Object initialization



# accessing the parent class 'Phone' attributes and mathods
# print(s.__price)         # private attribute will throw error hence commented here
print(s.model_year)
print(s.brand)
print(s.Phone_memory('128GB'))    # accessing parent class's method

'''  Note : 'getter()' function will give the 'Private attributes' of 'Parent class' using Child class's object  '''


# --------------------------------------------------------------------------------------------------------------------------------------- #

''' Method Overriding : If same 'methods' are present in 'Parent' and 'Child' class then using Child class object, Child class method will only be called not 'parent' one'''
# But parent method can be called usinf 'Parent' class object only

class Phone:

    def __init__(self , price , brand , camera):
        print("I am Inside Phone Constructor")
        self.price  = price 
        self.brand  = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone from Phone Class")

class SmartPhone(Phone):

    def buy(self):
        print("Hehehe , Buyng a SmartPhone ")


p = Phone(20000 , "Samsung" , "20MP")
s = SmartPhone(20000 , "Samsung" , "20MP")

# 'Method overriding' as the child's class method is called not parent class
s.buy()


# ----------------------------------------------------------------------------------------------------------- #

''' Super Keyword : Used to trigger the parent/child class constructor/methods ,depend upon the using case '''
''' Super Keyword cannot be used outside the class '''
# Example - 1
class Parent:

    def __init__(self , name , gender):
        print("I am in the Parent class")
        self.__name = name
        self.gender = gender

    def get_info(self):
        print("Parent Class hai re baba")

class Child(Parent):

    def get_info(self):
        print("Child Class mein hai re baba")
        super().get_info()                            # executes the parent class method 'get_info'
    
    
son = Child("Aashish" , "Male")

son.get_info()   

'''Execution Stage of son.get_info()-
    # step-1 => executes the parent class instructor
    # step-2 => executes own class method i.e. get_info()
    # step-3 => executes the same parent class method i.e. get_info()
'''

# Example - 2
class Phone:

    def __init__(self , price , brand , camera):
        print("Inside the Phone class Constructor")
        self.price  = price 
        self.brand  = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self , price , brand , camera , os , ram):
        print("Inside SmartPhone Constructor")
        super().__init__(price , brand , camera)                     # executing/triggering the Parent Class( Phone ) constructor
        self.os = os
        self.ram = ram
        print("Inside the SmartPhone Constructor")


s = SmartPhone(20000 , "Samsung" , 12 , "Android" , 8)    # child class ( SmaetPhone ) object

print(s.os)
print(s.brand)

''' Note : super() keyword always used inside the class not outside the class '''


# --------------------------------------------------------------------------------------------------------------------- #

''' Inheritance summary:
    1- A class can inherit from another class
    2- Inheritance improves code re-usability
    3- Public Constructor , Public attributes , Public methods get inherited to the child class
    4- The parent has no access to the child class
    5- Private properties of parent class are not accessible directly in child class ( use getter() function to access them )
    6- Child class can override the attributes or methods. This is called 'Method overriding'
    7- super() keyword is an in-built function which is used to invoke/trigger the parent class's methods and constructors
'''

# ---------------------------------------------------------------------------------------------------------------------- #

''' Types of Inheritance
    1- Single Level Inheritance : One parent class - One child class
    2- Multi-level Inheritance  : Child class is connected to further parent,granparent classes on it's head ( both directions may have classes till any long )
    3- Hierarchical Inheritance : One Parent and multiple child classes ( bantwara of property )
    4- Multiple Inheritance     : single class inheriting from multiple parent classes ( parent class - mother and father , child class - children )
    5- hybrid Inheritance       : hierarchical + multiple + single
'''
# ----------------------------------------------------------------------------------------------------------------------- #

''' Polymorphism : Having multiple phases. Same thing behaves differently at different positions/conditions
    ~ 3 main concepts in Polymorphism
        1- Method Overriding    : During inheritacne, When same function in parent and child class is called then only child class's method is gonna triggerred
        2- Method Overloading   : In a single class, you have multiple methods of 'same names' but 'Outputs are different' on the basis of arguments you provide ( Why Need of Method Overloading : improves readability of the code ). Python doesn't support it.
        3- Operator Overloading : Operator( example : + operator ) behaves differently when used on different inputs given
'''

# Method Overloading
# Implementation of Method Overloading in Python using default and positional arguments concept
class Shape:

    def Area(self , a , b= 0 , c = 0):
        if b==0 and c==0:                         # area of circle
            return 3.14 * a * a
        elif a!=0 and b!= 0 and c==0:             # area of rectangle
            return a * b
        else:
            return a * b * c                      # area of cube
        
s = Shape()    # object initialization

# printing as the 'Area' method as per the given arguments inside it
print(s.Area(2))
print(s.Area(2 , 3))
print(s.Area(2 , 3 , 4))


# Operator Overloading implementation
print('hello' + 'world')                     # concatenation
print(4 + 5)                                 # sum of two numbers
print([1 , 2 , 3] + [4 , 5])                 # list merging

# ------------------------------------------------------------------------------------------------------------------ #

''' 
Abstraction : Means hiding the implementation details and showing only the essential features to the user.
            ~ It focuses on what an object does rather than how it does.
            ~ Abstract class must consist atleast one 'abstract method' inside the class using '@bastracmethod' decorator

Why Abstraction : To reduce complexity, increase reusability and improve maintainability.

Abstract Class consists of an 'abstrat method' which doesn't have anything written inside it

Example : When using TV remote, we only press buttons( power, volume , etc) but we don't know the functioning behind them
'''

from abc import ABC, abstractmethod            # importing 'ABC( Abstract Base Class )' and 'astract method' from 'abc' module

class BankApp(ABC):           # inheriting from 'ABC' base class makes it an abstract class
  
    def Database(self):
        print('Connected to Database successfully')

    @abstractmethod          # using '@abstractmethod' decorator, it becomes an absract method of abstract class
    def security(self):
        pass


class MobileApp(BankApp):    # inheriting the 'BankApp' class here

    def mobile_login(self):
        print("Mobile Login Successful")

    def security(self):      # creating of 'abstract method' is mandatory here otherwise object of this class cannot be 'instantiated'( can't initialize )
        print("Security process is done")


mob = MobileApp()      # object initialization only when abstract method is present
bank = BankApp()       # abstract class's object can't be instantiated


# accessing the methods of any class above
mob.Database()
mob.security()         # this security() method is from it's own class i.e. 'MobileApp class'
mob.mobile_login()
