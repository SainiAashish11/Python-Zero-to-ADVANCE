c = int(input("enter the number for 'c' : "))
d = int(input("enter the number for 'd' : "))
    
sum1 = c + d
print("the sum is : " , sum1)
age = int(input("enter your age first : "))  

if(sum1 <=10):
        print("sorry! you are much far from the number")

elif(sum1 > 10 or sum1 <= 25):

    if(sum1 <= 15):
        print("yes! you are nearby to 25")

    elif(sum1 <= 20): 
        print("hey hurre! you are very close now")
    
    elif(sum1 < 25):
        print("very very close now")
    
    elif(sum1 == 25):

        if( age == 21):
            print("you are eligible to move forward now")  
        
        else:
             print("you are not eligible")    

    else:
        print("number is larger than 25")
