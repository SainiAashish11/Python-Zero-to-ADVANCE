'''
    Local Variable : Variable which is defined within the function or the private class
    and can be accessible only inside the scope of these, not outside
'''

''' 
    Global Variable : Variable defined outside the function or in public class and is
    accessible anywhere in the code
'''
# assigning a value to a variable
x = 4       # Global Variable
y = 9       # Global Variable
print(f"Global x : " , x)   
print(f"Global y : " , y)

# function 
def local_variable():
    global x , y          # calling global variable 'x' and 'y' in the function by 'global' keyword
    x = 10                # global x changed from 4 => 10
    y = 5                 # Local variable and is accessible inside this function only
    z = 2
    print(f"Local x : " , x)
    print(f"Local y : " , y)
    print(f"Local z : " , z)

local_variable()
print(x)               # taking the new value of 'x' from the function only coz we've accessed it as global variable
print(y)               # taking the new value of 'y' from the function only coz we've accessed it as global variable

# print(z)             # causing an error coz this is the local variable of the function only