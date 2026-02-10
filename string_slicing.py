''' slicing means by various string operations you can print any index value of the string'''


fruit = "apple"

len1 = len(fruit)              # len() function calculate the lenght of given string
print(len1)                    # printing the length of fruit
print(type(len1))

print(fruit[0:5])              # here 0 is index and 5 is total length(index 4)
print(fruit[0:2] + fruit[2:len(fruit)])    # concat of two strings

# note : '-' index is counted from the end of the string
print(fruit[0:-1])             # here -1 is written as len(fruit)-1 , '-1' is exclusive
print(fruit[0:len(fruit)-1])
print(fruit[-4:5])             # here -4 is len(fruit)-4  or counted from back as -1,-2,-3 and -4
print(fruit[-4:-2], "\n")      # here -4 and -2 both are len(fruit)-4 and len(fruit)-2



# [start : end : step]

print(fruit[::2])              # here ::2 used for printing only second character from the string but started from 'first' index
print(fruit[::-1])             # here ::-1 used for reversing the string
# [::-1] => means 'start' index is now the 'end' index of the string and vice-versa => start and end is swapped
'''Applicability: The [::-1] slice works on any sequence type (e.g., strings, lists, tuples) 
   but not on non-sequence(unordered data type) types like sets, dictionaries or integers '''

for i in fruit:                # initializing the loop where 'i' is the loop variable and 'i' starts from '0' to 'length-1 = 5-1 = 4' of the 'apple'
    print(i)                   # taking indices values by variable 'i' as i=a , i=p , i=p, i=l , i=e

print("\n")                    # for next line

for i in fruit:
    print(str(i))              # specifying 'fruit' as a string using str() function and accessing the string characters as str(i)         

# note: print() function adds the new line by default as str() function returning 'newline' and converted 'alphabet' into string to print() function after every iteration
print("\n")


integers = [0,1,2,3,4]
for i in integers:
    print(integers[i])         # here 'i' is not the index but the value of the list itself => i=0 which results in integers[0] = 0


# accesing the indexes as values of list itself
lst = [10 , 20 , 30]
for i in lst:
    print(lst[i])              # values of i = 10,20,30 and there are no such indexes in 'lst' list => index error


fruit = 'apple'
for i in fruit:  
    print(i , end=' ')         # here end=' ' is adding single space after every character printed



