''' Recursion : It is a technique where a function calls itself in a loop so there is no need to 
                implement a loop to call the function more than one time

~ Recusrion uses the 'Stack' data structure to implement the logic
'''

''' Iteration vs Recursive approach'''
# Iteration - solving problem using loops
# Example : multiply of two numbers
def multiply(a , b):

    result = 0
    for i in range(b):
        result = result + a
    print(result)

multiply(2 , 3)

# Recursive approach : 1- Know the base case
#                      2- Break down the problem into small problem of same kind
# Example : multiplication of two numbers
def mul(a , b):

    if b == 1:       # base case
        return a
    else:
        return a + mul(a , b-1) 
    
result = mul( 2 , 3)    # storing the return value in 'result' variable
print(result)


# Example : Palindrome ( aage peecghe se ek barabar )
# Base condition : if len(string) == 1 => 'a' = 'a' only which means aage peeche se ek barabar
def palindrome(string , org_string=None):

    # code for storing the original string to print at the output when it is a 'Palindrome'
    if org_string is None:
        org_string = string


    # main code of plaindrome starts from here
    if isinstance(string , str):
        if len(string) <= 1:
            print('String is Palindrome : ' , org_string)
        else:
            if string[0] == string[-1]:
                palindrome(string[1 : -1] , org_string)        # string[1 : -1] slices the 'first' and the 'last' character and retruns the 'left substring' part
            else:
                print('Not a Palindrome')
    else:
        print("Invalid Input given")
            
        
# function calling with valid string inputs
palindrome('madam')
palindrome('malayalam')
palindrome(2)

''' Procedure of above recusrion in Stack memory:

How recursion unfolds (trace for "madam")

Call stack:

palindrome("madam", None)
   -> org_string = "madam"
   -> string[0] == string[-1] ("m" == "m") ✅
   -> recursive call: palindrome("ada", "madam")

palindrome("ada", "madam")
   -> org_string = "madam" (kept from earlier)
   -> string[0] == string[-1] ("a" == "a") ✅
   -> recursive call: palindrome("d", "madam")

palindrome("d", "madam")
   -> len("d") <= 1 ✅
   -> print("String is Palindrome :", "madam")
'''

# ------------------------------------------------------------------------------------- #

''' Rabit Problem : 
1- in a pen, 2 Rabits are placed at 0th day of first month ( starting day )
2- pair of Rabits can produce only male and female offsprings after reproduction
3- pair can reproduce once they aged 1 month completely

Question : How many pair of rabits will be present in pen after 12 months
'''
import time
def fib(m):               # 'm' are the months in integer
    if m == 0 or m ==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)

start = time.time()                 # time before starting the program
print(fib(12))                      # after 12 months => pair of rabits
print(time.time() - start)          # time after executing the program

# Note : Fibonacci series discovered after this problem '''
''' This recursive solution will take so much time for bigger months like 40,48, and so on
so to handle that problem we need to implement the 'Memoization' techinique.
~ Memoization : Time-Space complexity tradeoff 
'''
import time
def memo(m , d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1 , d) + memo(m-2 , d)      # dictionary 'd' is updating everytime with 'two previous months' values
        return d[m]                 # returning the 'value' of month 'm'

  
d = {0:1 , 1:1}
start = time.time()
print(memo(48 , d))                  # calculating fib value for '48' months with intial dictionary 'd' = {0:1 , 1:1}
print(time.time() - start)

''' Complexity:
Time: O(n)  — because each 'm' is computed once, then cached in the dictionary
Space: O(n) — the dictionary holds results for 0 to 'm' inputs => m+1 inputs'''