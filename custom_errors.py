# Raising custom_errors : for throwing custom errors using 'raise'

# Example - 1
a = int(input('Enter the value between 5 and 9 : '))

if ( a < 5 or a > 9):
    raise ValueError('Value should be between 5 and 9')



# Example - 2
salary = int(input('Enter your Salary : '))
if not 2000 < salary < 5000:
    raise ValueError('Not a valid Salary')

'''
Note : This is useful because sometimes we might want to do 
something when a particualar exception is raised. For ex: 
sending an error message to the admin like : calling an API
'''

salary = int(input('Enter your Salary : '))
if not 2000 < salary < 5000:
    raise ValueError('Salary is not valid')
