''''match case' : It is same as 'if_else' functioning but we don't need to write like 'if-else' again and again. It functions as to compares
    the value of the variable and provides the result accordingly
    
'''


player_number = int(input("Enter your player number to play : "))    # roll number input from user


if( player_number >=20):
    
    x = int(input(" Enter the mode you want to play : "))               # 'x' variable input from user

    match x:                                                            # 'match' is the function to match the 'x' variable with different 'cases'

      case 0 : 
        print("Welcome to the new game")

      case 1 :
        print("This is the first level of your game")
    
      case 2 :
        print("This is the third level of game")

      case 3 :
        print("Welcome to the final round")
      
      case _ :                                                        # this is by 'default case' which runs when no other 'case' matches
       
       print("This is default case. Please choose valid mode")

else:
    print("You are not allowed to play! SORRY")  

# Note : In Python, you don't need to write 'break' statement after every 'case' as by default it breaks and ends the program but in 'C/C++' 
#        we need to write the 'break' statement after every 'case'


