# Recursion : When we call same function inside that function

def factorial(n):
    if(n == 0 or n == 1):   # '0!' and '1!' equals to '1'
        return 1
    
    else:
        return n * factorial(n-1)     # working : 5 * factorial(4) ---> 5 * 4 * factorial(3) ---> 5 * 4 * 3 * factorial(2) ---> 5 * 4 * 3 * 2 * factorial(1) = 120    
    
# Note : when 'return' is returning the value of 'n * factorial(n-1)' to the 'function' and it stores there to evaluate further factorials untill it reaches the end result

print(factorial(5)) 
print(factorial(0))
print(factorial(1))


# Note : Functioning of Recursive calls and return together
'''How return Works Across Calls in factorial(5)

# Let's go through the call stack for factorial(5) and see how each return statement builds up to the final result.
# factorial(5) returns 5 * factorial(4).
# This call won't finish until factorial(4) returns.

# factorial(4) returns 4 * factorial(3).
# This call won't finish until factorial(3) returns.

# factorial(3) returns 3 * factorial(2).
# This call won't finish until factorial(2) returns.

# factorial(2) returns 2 * factorial(1).
# This call won't finish until factorial(1) returns.

# factorial(1) hits the base case and returns 1.
# Now, each call in the stack can resolve one by one:

# factorial(2) returns 2 * factorial(1) = 2 * 1                  ^
# factorial(3) returns 3 * factorial(2) = 3 * 2 * factorial(1)   |
# factorial(4) returns 4 * factorial(3) = 4 * 3 * factorial(2)   |
# factorial(5) returns 5 * factorial(4) = 5 * 4 * factorial(3)   |
'''