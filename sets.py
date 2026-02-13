# Set : Unordered collection of any data items and is 'immutable' once created
# you cannot access set data items with the'index' number coz they are randomly distributed and hence 'index' changes every time we go through the 'set' elements

s = { 2 , 5 , 4 , 6 , 7 }
print(s)


# empty set
a = {}          # it is a dictionary if only '{}' used
print(type(a))

a = set()       # empty set 'a' is created
print(type(a))

# accessing set data items using 'for loop'
s = { 2 , 5 , 4 , 6 , 7 }
for values in s : 
    print(values)



