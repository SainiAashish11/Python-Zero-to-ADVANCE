# List methods : These are the methods to perform various tasks on list
 
l = [2,4,1,8,5,6,3,7,5,8,3,4]
print(l)

# append
l.append(9)             # adding '9' into the list
print(l)

# appending the dictionary
l = [2,4,1,8,5,6,3,7,5,8,3,4]
dict = {" Animal" : "Monkey" , "Age" : 2}
l.append(dict)
print(l)

# sorting ascending and descending
# ascending
l = [2,4,1,8,5,6,3,7,5,8,3,4]
l.sort()                # 'sorting' the list into the 'ascending order' :- default sort = ascending
print(l)

# descending - method 1
l = [2,4,1,8,5,6,3,7,5,8,3,4]
l.sort(reverse = True)    # 'sorting' the list into 'descending order' ( True => ascending , False => descending ) , this method modifies the original list
print(l)
# descending - method 2
l = [2,4,1,8,5,6,3,7,5,8,3,4]
sorted_copy = sorted(l , reverse = True)   # this doesn't modifies the original list
print(sorted_copy)
print(l)                  # to check whether the original list 'l' is changed or not

# Sort with 'key'
words = ["apple", "banana", "kiwi", "fig"]
words.sort(key=len)      # sorting on the basis of 'length' of the words
print(words)


# reverse
l = [2,4,1,8,5,6,3,7,5,8,3,4]
l.reverse()             # reverse the original list in the memory
print(l)

# reversed() function for a copy of same 'new list'
l = [2,4,1,8,5,6,3,7,5,8,3,4]
new_list = list(reversed(l))     # doesn't modifies the original list
print(new_list)
print(l)


#indexing : to find the index of given value
l = [2,4,1,8,5,6,3,7,5,8,3,4]
print(l.index(2))       # giving the index of first incoming '2' in the list


# counting
l = [2,4,1,8,5,6,3,7,5,8,3,4]
print(l.count(3))       # giving the number of count of '3' in the list 
# Note : 'l.count()' and 'l.index()' should be written with 'print' statement as 'print(l.count())' or store in a 'variable' first then print



# list 'm' becomes 'l' and change to 'm' will be happening in 'l'
l = [2,4,1,8,5,6,3,7,5,8,3,4]
m = l                   # list 'l' contents are going to list 'm' and now any change to 'm' will be reflected in 'l'
m[0] = 1            
print(m)          
print(l)


# copying
l = [2,4,1,8,5,6,3,7,5,8,3,4]
m = l.copy()
m[0] = 0
print(m)
print(l)
# Note : List 'l' and 'm' are different now coz any change in 'm' will not reflected in 'l'


# inserting : It inserts new element at particular index
l = [2,4,1,8,5,6,3,7,5,8,3,4]
l.insert(1 , 11)        # '1' is index and '11' is new element to be inserted
print(l)

# extend : It adds the entire new data type(list , set , tuple , dictionary ) at the end of the list

l = [2,4,1,8,5,6,3,7,5,8,3,4]
rainbow_colours = ["violet" , "indigo" , "blue" , "green" , "yellow" , "orange" , "red"]
l.extend(rainbow_colours) 
print(l)

# but in 'dictionary' it only iterates over the 'keys' not on the 'values' so only 'keys' will be added to the 'new list'
l = [2,4,1,8,5,6,3,7,5,8,3,4]
city_info = { 'Location' : 'Bangalore' , 'PinCode' : 560001 }
l.extend(city_info)
print(l)


# concatenating the lists
l = [2,4,1,8,5,6,3,7,5,8,3,4]
m = [11, 12, 13, 14, 15, 16, 17]
k = l + m
print(k)

