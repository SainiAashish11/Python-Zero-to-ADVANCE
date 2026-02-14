'''
Exception handling : It is the process of responding to unwanted or 
unexpected events when a program runs. Exception( error ) handling deals to avoid 
the program or system crashing
'''
# Python has many 'built-in exceptions' that are raised when our program encounters an error
# We'll read these 'exceptions' in future 

''' 
When these exceptions occur, the python interpreter stops the current process and passes it 
to the calling process until it is handled, if not handled then the program will crash
'''

try:    # try this code if workis then fine otherwise go to 'except' block
    a = int(input('Enter the value of a : '))
    for i in range(1,11):
        print(f'Table of a is : {a} * {i} = {a * i}')

except ValueError:         # execute if 'try' didn't work
        print("This is not a valid input")



# except inside except for multiple resolutions

try:
    num = int(input('Enter the Value you want : '))   # getting 'int' input from the user
    l = [1 , 2 , 3 , 4 , 5]
    print(l[num])            # accessing the list items from user entered 'num' value

except Exception as e:
    print(e)