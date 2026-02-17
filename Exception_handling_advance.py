'''
    There are 2 stages where error may happen in a program
      1- During Compilation -> Syntax error
      2- During Execution   -> Exceptions
'''
  
'''
   Syntax Error
      1- Something in the program is not written according to the program grammar
      2- Error is raised by the interpreter/compiler
      3- You can solve it by rectifying the program/code by debugging it
'''

# Types of Errors:
# 1- IndexError : When trying to access an item at an invalid index
L = [ 1 , 2 , 3]
print(L[100])         # IndexError: list index out of range


# 2- ModuleNotFoundError : When incorrect module or wrong module spelling is imported
import maths          # 's' should not be there at the end of 'math'


# 3- KeyError : When a key is not found
D = { 'name' : "Aashish"}
print(D['age'])


# 4- TypeError : when an operation or function is applied to an object of an inappropraite type
print(1 + 'a')       # 'integer + string' is not possible


# 5- ValueError : when a function's argument is of inappropriate type
int('a')             # ValueError: invalid literal for int() with base 10: 'a'4


# 6- NameError : when an object could not be found
print(k)             # 'k' was never initialized


# 7- AttributeError : when an unsupported function or operation is performed on a data type which doesn't exists in the 'class of that data type'
l = [1 , 2 , 3]
l.upper()            #AttributeError: 'list' object has no attribute 'upper'

# ----------------------------------------------------------------------------------------------------------#

''' Exceptions : If things go wrong during the execution phase
    1- Memory overflow
    2- Divide by 0 -> logical error
    3- Database error  

    Two main reasons for Exception Handling :
    - User interaction smooth
    - Security breach : if someone will get to know the exact error in the code then exception handling hides that error   
'''
# Try - except block : If error occured then that code will be added in 'try' block and what to do after that error will be added in 'except' block
# If any code is doing external stuff like opening a file, Loading Database, connecting a Device) then always add that piece of code in 'try-except' block

# Example :
with open('sample.txt' , 'w') as f:
    f.write('Hello World')
# opening a wrong file in 'try-except' block so that user experience should become smooth
try:
    with open('sample3.txt' , 'r') as f:
            print(f.read())

except:
     print("Sorry File Not Found")

#----------------------------------------------------------------------------------------------------------#

# catching specific error with multiple 'except' blocks
try:
    m = 5
    f = open('sample.txt' , 'r')
    print(f.read())     # printing the file content
    print(m)            # printing 'm' value
    print(5/0)          # division with '0'

except FileNotFoundError :
    print("file not Found")
except NameError :
    print("Variable not defined")
except ZeroDivisionError :
    print("Zero Division Is not Possible")
except Exception as e:
    print(e)                   # by default error will execute this block withy specific error

# Note: Always use 'default-error block' at the end of the 'try-except' block otherwise this will overlook other 'except' messages

# ---------------------------------------------------------------------------------------------------------#

# else block : After the successful execution of 'try' block, 'else' block will be executed means no error occured in the program

try:
     f = open('sample.txt' , 'r')
except FileNotFoundError:
     print('File Not Found')
except Exception as e:
     print(e)
else:
     print(f.read())

# ---------------------------------------------------------------------------------------------------------#

# finally : excution will occur in any case whether error occured or not
# mostly used for closing the work ( ex: file close , database connection close , connection of device close , etc )

try:
     f = open('sample.txt' , 'r')
except FileNotFoundError:
    print('File Not Found')
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print('This will be executed at any case')

# ---------------------------------------------------------------------------------------------------------#

# raise exception : power to programmer to 'raise' any type of error in the code

raise FileNotFoundError('File is not present')

# class example with 'raise exception'
class Bank:
    def __init__(self , balance):
        self.balance = balance

    def withdraw(self , amount):
        if amount < 0:
            raise Exception('Amount cannot be negative')
        if self.balance < amount or self.amount > amount:
            raise Exception('Not Enough Money')
        self.balance = self.balance - amount
    
obj = Bank(10000)     # initializing 'Bank class' object as 'obj' with 'amount' as '10000'

try:
    obj.withdraw(50000)     # amount > balance hence 'raise exception' will occur
except Exception as e:       # this exception will catch 'raise exception' from 'withdraw' function
    print(e)
else:
    print(obj.balance)


# ---------------------------------------------------------------------------------------------------------#

# Custom Exception 

class SecurityError(Exception):          # custom exception class

    def __init__(self , message):
        print(message)

    def logout(self):
        print('Logging out from all the devices')

class Google:                            # class Google for login credentials info

    def __init__(self , name , email , password , device):    # '__init__ constructor' for initializing the class variables
        self.name     = name 
        self.email    = email
        self.password = password
        self.device   = device
    
    def login(self , email , password , device):              # 'login function' for checking the valid login credentials
        if device != self.device:
            raise SecurityError('There is a login with other device')
        if email == self.email and password == self.password:
            print('Welcome')
        else:
            print('Login Error')
    
obj = Google('Aashish' , 'Aashish@gmail.com' , '1234' , 'android')     # creating a 'Google' class object as 'obj'

try:
    obj.login('Aashish@gmail.com' , '1234' , 'windows')
except SecurityError as e:             # this 'except' block will 'catch' the error from the 'login' function in the 'Google' class
    e.logout()               # accessing the 'logout' function via 'e' variable
else:
    print(obj.name)          # printing the 'name' of the user after successful 'try' block execution
finally:
    print('Database connection is Closed Now')