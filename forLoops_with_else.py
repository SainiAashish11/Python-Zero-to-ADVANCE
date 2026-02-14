# Note : 'else' will be executed when all the iterations finished but if we break the 'for loop' in the between then 'else' will not be executed

for i in range(5):
    print(i)

else:
    print(f"{i+1} is not present")    # 'i=4' here hence => i+1 = 5



# When we break the 'for loop' in between

for i in range(5):
    print(i)
    if i == 4:
        break        # after breaking out the 'for loop' , 'else' will not be executed

else:
    print("No more i")

# Note : In Python, the 'else' block in a 'for loop' only executes if the loop completes normally — that is, without encountering a 'break' statement. If the loop ends due to a 'break', the 'else' block is skipped.
# The 'else' block is like a final check: "If I didn’t find what I was looking for, do this." Thus, the 'else' block is only executed if the loop completes all iterations without interruption.



# .format() 

for i in range(5):
    print("iteration no {} in for loop".format(i))     # .foramt() is inserting the values of 'for loop' between the {} brackets in the string
          
else:
    print("no more iterations...")
    