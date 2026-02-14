# Finally : Anything written inside the 'finally' clause will be executed no matter what happens
# This is generally used to conclude the important tasks/events in the programming


# Normal 'try-except-finallly' 
try:
    list = [1 , 2 , 3 , 4 , 5]
    a = int(input('Enter your index :'))
    print(list[a])

except:
    print('Some error occurred')

finally:
    print('I always executed')     # this block always executed


# 'try-except-finally' inside the function( def ) : this is the main concept that 'finally' is mostly used in functions for performing sure-shot tasks or endings
# coz when function returns something then it should be stopped executing but still 'finally' block has to be executed even after the 'return'

def func():
    try:
        lst = [1 , 2 , 3 , 4 , 5]
        user_input = int(input('Enter your index in interger : '))
        print(lst[user_input])
        return 1

    except:
        print('Some error occurred')
        return 0
    
    finally:
        print('I always executed')

x = func()   # function call

# Note : whether function is returning '1' or '0' after 'try/except' block but still 'finally' block is executing


