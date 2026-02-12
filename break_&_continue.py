# 'break' used to stop the overall iteration or it stops the loop it lies within  
i = 0

while(i<=10):
    if(i==5):
        break                           # breaking the while loop when 'i' becomes '10'
    print(f"5 x {i+1} =  {5*(i+1)}")
    i += 1                              # here this is incrementing the 'i' in while loop otherwise it will become an infinite loop

print('\n' , f"The value of i is {i} right now" , '\n')

''' Note : After executing the 'break' statement when 'i == 5 then loops exits and 'print' and 'i += 1' conditions will be skipped'
only outer 'print' condition will execute
'''


# continue : it is used to skip the particular iteration 
for i in range(15):
    if(i==10):
       continue                         # skipping the 'i=10' iteration and going ahead
    print(f"5 x {i} = {5*i}")


# do-while loop - it executes the iteration atleast once and then depending upon the further conditions
print("\n")                             # for going into new line
i = 0
while True:                             # this condition is always 'true' hence this is an infinite while loop acting as 'do' atleast one time
    print(i)
    i += 1
# till here above part is acting as do-while coz while body is executing atleast once and then depending upon 'if' condition
    if(i % 10 == 0):                      # checking whether number 'i' is divisible by 10 or not
        break  
    # breaking out of the 'while loop' when condition is satisfied ( 10 % 10 == 0)

''' Note : If the divisor is larger than the dividend, the remainder is simply the dividend itself.
if: a < b -> a % b = a 
'''