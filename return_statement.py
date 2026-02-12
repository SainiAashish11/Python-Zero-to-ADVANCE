'''Return statement : when function calling happens , it stores the returned value into the new created variable
   - When there is return statement we have to store it into a new variable always if we have to use that return value of function anywhere in the code'''

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)  # here 'len(numbers)' is calculated already during 'numbers' provided in the function call 
    
c = average(2,3)             # value of 'average' stored in 'c' 
print(c)

average(5,2)                 # calculating the 'average' but not providing it's result anywhere until it will not be stored into a new varaible and then printed
print(average)               # this is printing the 'hexadecimal' address value of function object name 'average'
