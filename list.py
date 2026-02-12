# List : It is an ordered collection of data(integer , string , bool , float , None , list , dict , tuple , set , functions , objects , etc)
# It is a 'mutable' data type in Python means we can modify the object value anytime required
# Square brackets [] are used to initialize a 'list' 

l = [1,2,3,4,5, "Aashish Saini" , True , 2.5 , None]
print(l)         # printing all the elements of 'list'
print(l[:])      # printing all the elements as 'starting' and 'ending' index are taken by default from '0 to len-1'


# indexing
print(l[3])         # accessing the 'third index' element
print(l[len(l)-1])  # accessing the 'last' element  
print(l[-3])        # accessing the 'third element' from the end as from end counting starts from '-1'
print(l[1:-4])      # printing from 'index[1]' to 'fifth element from end' as '-4' is excluded
print(l[0::2])      # jumping case : taking every second value from the given 'starting' index


# checking whether data present in list or not
if "Aashish Saini" in l:
    print("YES ,Present")

else:
    print("NOT Present, Sorry!")


# List comprehension : creating list by 'for-loop' and 'conditions' with other data types
lst = [i for i in range(4)]                                    # creating list as 'i' is iterable object
print(lst)

ast = [ i*i for i in range(4)]
print(ast)

bst = [ i*i*i for i in range(4) if i%3==0]                       # creating list with 'if' condition
print(bst)

name = ["aashish" , "saini" , "aashishSaini" , "SainiAashish"]   # list of 'string' values
name_0 = [i for i in name if "sh" in i]                          # creating new list with condition
print(name_0)    


# Mutability of a 'List' : if a == b → hash(a) == hash(b)
my_list1 = [1 , 2 , 3 , 4]
my_list2 = [1 , 2 , 3 , 4]

print(my_list1 == my_list2)                   # both lists are equal in identity address(id) because pointing to same memory location 
print(hash(my_list1) == hash(my_list2))       # as lists are not hashable, hence their hash values cannot be calculated so this line will show error


# .append() modifies the list in-place
my_list1 = [1 , 2 , 3 , 4]
my_list1.append(5)
print(f"List after append: {my_list1}")
print(f"Memory address after append: {id(my_list1)}")             # Address will be the same


# Concatenation (+) creates a new list with a 'new address'
my_list1 = [1 , 2 , 3 , 4]
my_list2 = [1 , 2 , 3 , 4]

print(f"Memory address after concatenation: {id(my_list1)}")
my_list1 = my_list2 + [6]                                         # this element will be added at the end of the 'my_list1'
print(f"List after concatenation: {my_list1}")
print(f"Memory address after concatenation: {id(my_list1)}")      # Address will be different
