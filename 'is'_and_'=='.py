# is operator : It compares the identity or exact location of the object in the memory
# == operator : It compares the values of the objects in the memory


# Example - 1 ( integer - immutable )
a = 4
b = 4
print( a is b)    # True coz integer is immutable and hence same memory location will be used 'by reference' by 'b' variable as well
print(hex(a))     # checking the location of 'a'
print(hex(b))     # checking the location of 'b'

print( a == b)   # True coz their values are same i.e. 4

# Example - 2 ( String - immuttable )
a = "Aashish"
b = "Aashish"
print(a is b)
print(a == b)


# Example - 3 ( tuple - immutabale ) 
a = ( 1 , 2)
b = ( 1 , 2)

print(a is b)
print(a == b)


# Example - 4 (set - immutable)
set_1 = ( 1 , 2 , 3 )
set_2 = ( 1 , 2 , 3 )

print(set_1 is set_2)
print(set_1 == set_2)


# Example - 5 ( list - mutable)
lst_1 = [1 , 2]
lst_2 = [1 , 2]

print(lst_1 is lst_2)      # False coz list is a mutable data type hence same location will not be shared now
print(lst_1 == lst_2)


# Example - 6 ( dictionary - mutable)
dict_1 = { 'name' : "Aashish"}
dict_2 = { 'name' : "Aashish"}

print(dict_1 is dict_2)
print(dict_1 == dict_2)


