# Tuples : Tuples are the ordered collection of data items
# () round brackets are used to store the data and it is an immutable data type.
# Data types that can be stored in a 'tuple' : numbers(Int , Float) , text( str ) , Booleans ( True , False ) , None , List[] , Dict{} , Tuple() , set{}, functions , class , an instance of a 'class' , a built-in function and lamda function

tup = (1 , 2 , 3 , 4 , 5 , "green" , "yellow" , True , 2.5 , None , [11 , 22 , 33])    # tuple is created
print(tup)                                                            # printing of tuple items
print(type(tup) , tup)                                                # getting 'type' and items within the tuple using 'type' keyword


# indexing
print(tup[2] , tup[3] , tup[5] , tup[4] , tup[-4])             # you can give multiple indexes in 'print' function
print("lenght of tuple is :" , len(tup) , " & " , "data items are :" , tup)


# checking data in 'tuple'
if "green" in tup:
    print( "YES present")

else:
    print("sorry ! not present")

