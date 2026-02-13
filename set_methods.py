# 'union' : Gives the new set consists of all elements(without repetition) and 'update' : Only updates the given set
#

s1 = {1 , 3 , 5}
s2 = {2 , 4 , 6}
print(s1.union(s2))    # direct output is returned from 'union' function
print(s1)              # s1 is not updated yet

print(s1.update(s2))   # here we can't get direct output as 'update' function returns 'none'
s1.update(s2)          # original set 's1' is updated first 
print(s1)              # updated set 's1'

# intersection and intersection_update

a1 = {"tokyo" , "madrid" , "barcelona"}
a2 = {"saharanpur" , "tokyo" , "madrid"}

print(a1.intersection(a2))        # direct output returned

a1.intersection_update(a2)        # original set 'a1' is updated
print(a1)                         # updated set 'a1'
 
# symmetric_difference : Gives the uncommon elements in a new set
# symmetric_difference_update : Updates the existing set

names1 = {"aashish" , "saini" , "akhil" , "khandelwal"}
names2 = {"rahul" , "saini" , "akash" , "khandelwal"}
print(names1.symmetric_difference(names2))               


names1.symmetric_difference_update(names2)
print(names1)

# difference and difference_update 

n1 = {12 , 1 , 2 , 47 , 13}
n2 = {5 , 12 , 1 , 13 , 19}

print(n1.difference(n2))       # n1 - n2 (printing all elements of 'n1' which are not in 'n2')
n1.difference_update(n2)
print(n1)


# isdisjoint() : check whether they have something common or not

n1 = {1 , 11 , 21 , 4 , 2}
n2 = {6 , 15 , 14 , 13 , 19}
print(n1.isdisjoint(n2))


# issuperset : set 1 consists of all set 2 elements or not

names1 = {"Aashish" , "Saini" , "Akhil" , "Khandelwal"}
names2 = {"Rahul" , "Saini" , "Aadarsh" , "Khandelwal"}
print(names1.issuperset(names2))


# issubset : checks that set lies within other set or not

print(names1.issubset(names2))

# add : it adds data item to set

s1 = {1 , 3 , 5}
print(s1)
print(id(s1))

s1.add(47)          # adding the data value '47'
print(s1)

print(id(s1))    # hash memory remains same coz the original set 's1' is changed with new values


# remove() / discard()
# Difference btw remove() and discard() : If element is not present in the set then 'remove()' raises an 'error' but 'discard()' doesn't

m = {1 , 2 , 3 , 4 , 5}
m.remove(3)
print(m)
m.discard(4)
print(m)

# Note : remove() and discard() functions are changing the original set


# pop() : it removes the random value from the set

m = {1 , 2 , 3 , 4 , 5}
item = m.pop()             # accessing the 'pop' data value
print(m)
print(item)


# del : It deletes the entire set

m = {1 , 2 , 3 , 4 , 5}
del m                    # it raises 'not defined' error as set is not existing after 'del'
print(m)


# clear : it clears the data values and set remains empty

y = {1 , 2 , 3 , 4 , 5}
y.clear()
print(y)


# if-else looping

m = {1 , 2 , 3 , 4 , 5}

if 3 in m:
    print("Present")

else:
    print("Not Present")