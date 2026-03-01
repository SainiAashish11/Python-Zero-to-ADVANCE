# making an Atm class with data entries from the users is : Card_no , Pin , Balance
        
class Atm:

    # global class variable which can be accesed by any object of this class and this variable is sitting in the class namespace
    bank_name = 'ICICI'

    # constructor
    def __init__(self , card_no , pin , balance):    # when class object is created with given parameters then this constructor is called with initialization of these variables
        # initialization of instance variables ( object values )
        self.card_no = card_no
        self.pin     = pin
        self.balance = balance

    
    # withdraw method
    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'Withdrawn of {amount} is Successful. Current Savings = {self.balance}'
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount
        return f'Deposited {amount}, New Balance = {self.balance}'
    

Atm1 = Atm('12345-6787' , 1234 , 5000)     # object-1 with user card details
print(Atm1.withdraw(2000))                 # accessing 'withdraw' function using object of the class


Atm2 = Atm('9870-6872' , 0000 , 2000 )     # object-2 with user card details
print(Atm2.deposit(5000))


print(Atm1.bank_name)        # accessing the bank_name which is a global class variable and can accessed by class objects only
print(Atm2.bank_name)

