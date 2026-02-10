a = int(input("enter the number for 'a' : "))
b = int(input("enter the number for 'b' : "))

sum = a + b 
print ("the sum is : " , sum)

if(sum>=20):      # if(expression) used to check whether the given expression is 'true' or 'false'
    print("numbers are strong")

else :            # when 'if' expression is 'false' then interpreter comes to 'else' expression for the evaluation
    print("numbers are not strong")


# now we'll see how 'if elif' statement  
if (sum <=10):
    print("you are not allowed to answer the question")

elif (sum <=15):   # 'elif' means 'if else'
    print("you can answer but only after voting")

elif (sum > 15 and sum <=25):
    print("you are eligible to answer but for 2 minutes")
    
else :
    print("yes ! you can freely answer")



