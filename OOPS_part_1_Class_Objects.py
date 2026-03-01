# Everything in the Python is an Object of classes => int , string , float  , None , Boolean , List , Tuple , Set , Dictionary
# Real world projects are not made with procedural approach ( line by line coding for each functionality )
# OOP is nothing but 'Generality to Specificity'
# A Programmer can make own Data Types using OOP


'''
OOPS : Object Oriented Programming
Principles of OOPS : 
    1- Object
    2- Class
    3- Polymorphism
    4- Encapsulation
    5- Inheritance
    6- Abstraction
'''

# Class : It is a Blueprint. Class is a set of rules and functionalities which can be followed or accessed using that class 'Object'
# Ex    : As a student of college, I can access or use my college facilities => 'College' is 'class' and 'I' am the 'Object'

L = [1 , 2 , 3]     # 'L' is the object of class list
print(type(L))


# Object : It is an instance of the 'class'
a = 5
b = "Aashish"
# 'a' and 'b' are the objects of class 'integer' and 'string' respectively


# Syntax to create an Object a class : object_name = Class_name()
I = int()     # int() is an int class
S = str()     # str() is a string class
L = list()    # list() is a list class
D = dict()    # dict() is a dictionary class
S = set()     # set() is a set class
T = tuple()   # tuple() is a tuple class




# How to make class
# 'class_name' should be written in Pascal Case ( every word start with capital letter and should be Sticked together)

class Atm:    # 'Atm' is the classname

    # Constructor(special function): We don't need to call constructor explicitly for it's execution
    # It is 'called' itself when the 'Object' of the class is formed

    def __init__(self):          # 'self' is the parameter which is must to provide in every constructor or function inside the class
        self.pin = ''            # initialization of 'pin' using 'self'
        self.balance = 0         # initialization of 'balance' using 'self'
        self.menu()              # menu() method is called using 'self'


# 0 - menu() function
    def menu(self):
        user_input = input("""
        Hi, How Can I Help You
        1. Press 1 to Create Pin 
        2. Press 2 to Change Pin 
        3. Press 3 to Check Balance 
        4. Press 4 to Withdraw 
        5. Exit' 
        """)

        if user_input == '1':
            # make create_pin function
            self.create_pin()

        elif user_input == '2':
            # make change_pin function
            self.change_pin()

        elif user_input == '3':
            # make check_balance function
            self.check_balance()
        
        elif user_input == '4':
            # make withdraw function
            self.withdraw()
        
        else:
            exit()    # exit() function for getting out


# 1 - create_pin function
    def create_pin(self):
        user_pin = input('Enter Your Pin : ')
        self.pin = user_pin

        user_balance = int(input('Enter you Balance Please : '))
        self.balance = user_balance

        print('Pin Created Successfully')
        self.menu()         # menu() function called so that continuity will be maintained in the code


# 2 - change_pin function
    def change_pin(self):
        old_pin = input('Enter Old Pin : ')

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input('Enter New Pin : ')
            if new_pin == old_pin:
                print('Pin is Same. Please Enter the New Pin')
            else:
                self.pin = new_pin
                print('Pin changed Successfully')
            self.menu()     # menu() function called for continuity

        else:
            print('You cannot change the pin')
            self.menu()     # menu() function for continuity


# 3 - check_balance function
    def check_balance(self):
        user_pin = input('Enter Your pin : ')

        if user_pin == self.pin:
            print('Your Balance is : ' , self.balance)

        else:
            print('Sorry! wrong Pin entered')
        
        self.menu()         # menu() function called for continuity


# 4 - withdraw function
    def withdraw(self):
        user_pin = input('Enter Your Pin : ')

        if user_pin == self.pin:
           # allow to withdraw
            amount = int(input('Enter the Amount You want to withdraw : '))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Withdrawl Successful. Balance is : ' , self.balance)
            
            else:
               print('Entered Amount is Invalid. Please Enter Valid Amount')
        
        else:
            print('Wrong Pin ! Sorry')

        self.menu()        # menu() function is called for continuity
           

# creation of Object of Atm class
obj = Atm()                # when the object of class 'Atm' is called 'constructor' is itself called and executed
print(type(obj)) 


# ----------------------------------------------------------------------------------------------------------------------------- #

''' Methods vs Functions '''
# Methods : It is a function but it is associated with an 'Object' 
# It is defined inside the class and the first parameter is usually 'self' ( whihc refers to the instance of the class )
# Methods are invoked on Objects ( instances of class )
# Ex :
class Sum:
    def sum(self , a , b):
        return a + b
    
obj = Sum()               # making object of class 'Sum'
print(obj.sum(2 , 3))     # accessing sum() method using class object


# Functions : It is a block of reusable code and independent of Objects ( but it can take Objects as parameter )
# It is implemented outside of the class and can be called from anywhere explicitly
# Ex :
def Sum( a , b ):
    return a + b

print(Sum(2 , 3))

''' 
Rule of Thumb :
    ~ If you see it written like => function(obj), it's a function.

    ~ If you see it written like => obj.method(), it's a method.
'''

# ------------------------------------------------------------------------------------------------------------------------------#

'''
 Concept of 'Self' : 'Self' as an argument for every method of the class, is nothing but 'object' of class only
~ Why need of 'self' : When a method inside the class wants to call any other method or data of the class then it can be done 
  only with the help of this 'self' object coz this 'self' becomes the initialized 'object' only
~ When an 'Object' of class is initialized then that 'Object' goes itself as an arguemnt in the method as 'self'
~ When multiple objects created in the class then 'self' always points to the 'latest Object' created in that class
'''

# ------------------------------------------------------------------------------------------------------------------------------#

# Magic methods ( Dunder Methods ) : Special methods and have special functionalities
# syntax : __name__
# Examples :
    # 1- constructor( __init__ ) 
    # 2- __str__  ( tells python interpreter how to print new data types )
    # 3- __add__  ( how to add data types )
    # 4- __sub__  ( how to subtratct data types )
    # 5- __mul__  ( hot to multiply data types )
    # 6- __truediv__  ( hoe to divide data types )

''' 
- Constructor : It is a method as it is defined inside the class and has super-power to execute itself when the object of class is just formed
  ~ Benefit of Constructor : Generally Configuration related code is written inside the 'constructor' that should be done without any user-permissions or handling
'''

# ------------------------------------------------------------------------------------------------------------------------------#

''' Creation of Own Data type using class and magic methods'''

# 1 - Fraction Data type ( a/b )
class fraction:
    # parameterized constructor : Constructor which expects inputs during the 'Object' creation
    def __init__(self , x , y):
        self.num = x                     # self.num is initialized with value 'x'
        self.den = y                     # self.den is initialized with value 'y'


    def __str__(self):                                  # '__str__' is a magic function which guides python to how to print the 'Object' of the class
       return '{}/{}'.format(self.num , self.den)       # string formatting using .format() , f-string => f'' formatting is also possible
    

    def __add__(self , other):                          # '__add__' is a magic function which guides python how to perform '+' operation on data types
        new_num = (self.num * other.den) + (other.num * self.den)       # cross-multiplication for 'resultant numerator'
        new_den = (self.den * other.den)                                # simple multiplication for 'resultant denominator'
        return '{}/{}'.format(new_num , new_den)
    

    def __sub__(self , other):                          # '__sub__' is a magic function which guides python how to perform '-' operation on data types
        new_num = (self.num * other.den) - (other.num * self.den)       # cross-multiplication for 'resultant numerator'
        new_den = (self.den * other.den)                                # simple multiplication for 'resultant denominator'
        return '{}/{}'.format(new_num , new_den)
    

    def __mul__(self , other):                          # '__sub__' is a magic function which guides python how to perform '*' operation on data types
        new_num = (self.num * other.num)                                # simple multiplication for 'resultant numerator'
        new_den = (self.den * other.den)                                # simple multiplication for 'resultant denominator'
        return '{}/{}'.format(new_num , new_den)


    def __truediv__(self , other):                      # '__truediv__' is a magic function which guides python how to perform '/' operation on data types
        new_num = (self.num * other.den)                                # simple multiplication for 'resultant numerator'
        new_den = (self.den * other.num)                                # simple multiplication for 'resultant denominator'
        return '{}/{}'.format(new_num , new_den)



fr1 = fraction(3 , 4)   # object initialization with arguments
print(fr1)
fr2 = fraction(2,5)     # object initialization with arguments
print(fr2)

# adding two fractions which will use '__add__' magic method
print(fr1 + fr2)

# subtracting two fractions which will use '__sub__' magic method
print(fr1 - fr2)

# multiplying two fractions which will use '__mul__' magic method
print(fr1 * fr2)

# dividing two fractions which will use '__truediv__' magic method
print(fr1 / fr2)