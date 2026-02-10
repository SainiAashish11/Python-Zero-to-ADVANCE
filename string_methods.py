# string can be modified using some in-built functions
# strings are immutable as you cannot change the string value once it is created with a hashing address( hashable object )

a = "///// aashish /////"
b= "aashish SaIni"
print(a.upper())                       # upper() function is not changing the 'a' string but creating new uppercase string
print(a.lower())                       # lower() function creating a new lowercase string hence we are saying 'strings are immutable'
print(a.rstrip("/"))                   # rstrip() function removes the 'trailing/end wale' characters provided inside the function
print(a.replace("aashish" , "saini"))  # replace() function replaces all the occurences of a string with another string
print(a.split(" "))                    # split() function splits the values as list elements on the basis of given character ( jaise yaha " " space ke base pe hamne split kiya )
print(b.capitalize())                  # capitalize() function capitalizes the first character of the string rest it will convert to lowercase
print(b.center(50))                    # center() function aligns the given string by given 'integer' input as a function value as 'center(integer)' 
print(a.count("/"))                    # count() function counts the number of times the charater repeats          
print(b.count("a"))
print(a.endswith("/"))                 # endswith() function gives 'true/false' if the given string is ending with the provided 'substring'
print(a.endswith("aa" , 3 , 9))        # endswith("string" , start_index counts from 0(by default) , ending_length(by default)) : returns the given 'substring' between the given 'indexes' 
print(a.find("a"))                     # find() function finds the first occurence of the provided 'substring' and gives index. If 'absent' returns 'False'
print(a.index("as"))                   # index() function finds the 'first-index' of the provided 'substring'

# Note : 'find()' function returns 'False' when substring is not found but index() function raises 'value error' and consists of exception handling -> ValueError: substring not found

print(b.isalnum())                     # isalnum() function only gives output 'True' when string is A-Z , a-z , 0-9 and "space should not be present into the string" and "mix of alphabets,numbers and characters should not be present"
print(b.isalpha())                     # isalpha() function is 'True' when string contains 'A-Z and a-z' otherwise 'False' and 'space should not be present in the string' 
print(b.islower())                     # islower() returns 'True' if all the characters in the string are in 'lowercase' otherwise 'False' and "not dependent upon space in the string"
print(b.isprintable())                 # isprintable() returns 'True' if string is printable otherwise 'False'

c = "aashish    SaIni\n"
print(c.isprintable())                 # here '\n' is not printable hence returns 'false'

d = "     "
print(d.isspace())                     # isspace() function returns 'True' only when string contains 'spaces'

e = "Aashish Saini Is A Student Of Iiit Dharwad"
print(e.istitle())                     # istitle() function returns 'True' if all the initial characters of the string are capital/uppercase otherwise 'False'

print(e.isupper())                     # returns 'True' if all the characters are 'uppercase' otherwise 'False'

print(e.startswith("Aashish"))         # returns 'True' if string starts with the given characters/string

print(e.swapcase())                    # swaps the strings in uppercase or lowercase with respect to the original string -> jaha lower vaha upper ho jayega and vice-versa 

f = "aashish saini is a student of iiit dharwad"
print(f.title())                       # returns the string with 'first character' in 'uppercase'