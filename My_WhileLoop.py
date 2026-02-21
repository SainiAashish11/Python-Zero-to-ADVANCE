# while loop used to execute statement till it is 'true' but when condition becomes 'false' loop comes out 
# they are of two types:
''' 1- incremented 
    2- decremented
'''
# incremented loop
start = 0

while(start <= 5):
    print(start)
    start = start + 1

print("\n")

# decremented loop
end = 5

while(end >= 0):
    print(end)
    end = end - 1

# while loop with '!=' operator
bool = False

while(bool != True):  # '!= True' means 'bool == False' so it will come inside 'while loop' first to check the condition and it got 'bool' = False
    print("bool is still false")
    bool = True
    print("Now bool becomes True")
    


 