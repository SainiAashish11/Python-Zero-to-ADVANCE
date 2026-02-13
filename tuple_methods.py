# Tuple cannot be changed once created ( immutability ) means only new tuple has to be introduced for any new requirement
# But we can convert tuple to list and then change that list accordingly

# defining the 'countries' variable
countries_and_position = ("India" , "America" , "Germany" , "Singapore" , "Japan" , 1 , 2 , 3 , 4 , 5)

# length of a tuple
print(len(countries_and_position))

# sorting ( default - ascending)
tup = (2,1,0,8,4,5,7)
print(sorted(tup))   # returns 'sorted' list not tuple
print(sorted(tup , reverse = True ))    # sorts in 'descending' order => True : Descending sort | False : Ascending sort




# converting 'tuple' into 'list'
countries_and_position = ("India" , "America" , "Germany" , "Singapore" , "Japan" , 1 , 2 , 3 , 4 , 5)
temp = list(countries_and_position)     # converting "countries" as a 'tuple' into a 'list' 


# appending
temp.append("Australia")   # adding 


# removing : removes specific 'element'
temp.remove("Singapore")   # removing paticular element
temp.remove(1)             # removing 'numeric' values as well
temp.remove(temp[2])       # removing element from '2' index
print(temp)


# reversing the tuple
countries = ("India" , "America" , "Germany" , "Singapore" , "Japan")
print(countries[::-1])

# Index : printing particular index value
new_tuple = (1,2,3,4,5,6,3,4,5,7,3,4,3,3,8)
print("first occurence of 4 is : " , new_tuple.index(4))  

'''Note : It raises value error(value not present) when 'element' is not present in the tuple'''
print(new_tuple.index(3 , 3 , 10))  # index(value , start , end) : finds how many times the 'element' is present in given range
print(len(new_tuple))               # length of tuple



# Tuple operations ( concatenation , count , slicing , repetition)
# concatenation of 2 tuples
name = ("Aashish" , "Simmy")
lname = ("Saini" , "Gundimeda")

result = name + lname   # new tuple with new memory address
print(result)


# count : returns the occurences of an elemnet in the tuple
new_tuple = (1,2,3,4,5,6,3,4,5,7,3,4,3,3,8)
print("Count of 3 is : " , new_tuple.count(3)) 


# slicing
new_tuple = (1,2,3,4,5,6,3,4,5,7,3,4,3,3,8)
print(new_tuple[2])
print(new_tuple[0 : : 2])         # printing values by jumping 2 places
print(new_tuple[::-1])            # reversing through slicing => new_tuple( start , end , step )
'''
When step is positive, Python travels left-to-right.
When step is negative, Python travels right-to-left
'''


# repetition : repeat the whole tuple
new_tuple = (1,2,3,4,5,6,3,4,5,7,3,4,3,3,8)
print(new_tuple * 2)


 