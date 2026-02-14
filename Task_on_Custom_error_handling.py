a = input('Enter a value between 5 and 9 or type \*quit*\ to exit: ')

if a == 'quit':
    print("Exiting the program")

else:
    try:     
        # when this block's condition will not fulfil then move on to 'except' block
        # two conditions 'b' should be 'int' and should be between '5' and '9'
        b = int(a)
        if not (5 < b < 9):
            raise ValueError('The number is not between 5 and 9')
        else:
            print(f"Success! You entered a valid number : {b}")

    except ValueError as e:
        print(f"Error is : {e}")
    
    


        


