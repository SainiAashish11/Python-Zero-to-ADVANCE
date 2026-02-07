name = "aashish"
surname = 'saini'

print(name[0])              # indexing the 0th element in the 'name' string  
print("-hello" , name)      # here single quoma(,) used to make "name"  as an arguement of print function 
print("-hello " + surname )    # '+' is used here to concat two string objects

a = '-hello sir this is Aashish Saini \"but i want to know who is your boss\" '    # Single quotations used to double quote the sentence by using back slash (\)
print(a)

b = '''-hello sir who are you if i ask your name, and this is Aashish saini from ECE IIIT Dharwad and also i want to ask your company profile. kindly send me your profile asap.'''
                                                                                   # inside triple single('''__''') or triple double("""__""")  quotes, we can write any string
print(b)


####################################################################################
# for loop in strings
for characters in name:
    print(characters)

print("\n")  # new line
    
for characters in surname:
    print(characters)

    