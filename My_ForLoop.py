# 'for loop' is the iteration method means when you have to execute individual/group statements by certain number of times 
# We have two types of loops in Python3 :
# 1- for loop
# 2- while loop
# strings , set{} , list[] , tuple() , dictionary{} are all 'iterable' data variables


# string iteration
name = "aashish saini"

for Name in name:            # here we are declaring the 'for loop' with 'Name' variable which is pointing at the first character of the 'name' variable and printing each characters iteratively
    print(Name)

print("\n")                  # new line


# string with 'end' operator
a = "aashish"
for i in a:                  # here 'i' will take every 'character' of the string and print on the console
   print(i , end = ",")      # here end="," is providing the ',' after every character of the 'aashish'
   
print("\n")



# range() function
for k in range(5):           # 'range()' function sets the range for the 'iteration' which starts from '0' and ends at 'n-1'
 print(k)

print("\n")

for k in range(0 , 5):       # '0' is the start(inclusive = which includes 0) point and '5' is the stop(exclusive = which doesn't include 5) point
   print(k)

print("\n")

for k in range(0 , 10 , 2):  #  here '2' is the gapping number which is taking every 'alternate' number from the pointed value, starts from '0' and ends at '9'
   print(k) 



# list []
list = [ "aashish" , 2 , 3 , "simmy" ]  # declaration of 'list' 
for i in list:                          # 'i' is the iterative variable here and taking each 'element' of the 'list' not each 'character'
   print(i)
print("\n")

# dict {}
dict = {"name" : "aashish" , "age" : 21 , "address" : "village telipura"}  # creating a dictionary with 'keys' and 'values'
for key, value in dict.items():                                            # key and value as a iterative operator , dict.items() is the function for accessing the dictionary items otherwise it'll show 'value error'
   print(f"{key} : {value} ")                                              # 'f' string method to print 'original key' and 'original value' inside the {} brackets
                                                                           # This makes f-strings very powerful and concise for embedding variables and expressions within strings.

# set {}
sett1 = { 1 , 2 , 3}                        # this is simple 'set' with no 'set inside set', hence values are iterable
for i in sett1:
   print(i)


sett2 = { 1 , 2 , 3 , frozenset({4 , 5})}   # 'set inside set' is not iterable due to hashing problem, hence converted to 'frozenset' for consistent hashing
for i in sett2:
   print(i)


# tuple()
tup = (1 , 2 , [1 , 2] , 'Ash')
for i in tup:
   print(i)