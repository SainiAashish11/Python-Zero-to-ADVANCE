# String formatting(old method) : It is used in string formatting using 'format' method

info = "My name is {} and I am from {}."   # {} curly brackets are called 'placeholders' in which values will be transferred by .format() function
name = "Aashish"                           # 'name' is the variable for placeholder
Place = "India"                            # 'place' is the variable for placeholder
print(info.format(name , Place))           # 'name' and 'place' are named arguments for '.format' function
print(info.format("Aashish" , "Uttar Pradesh"))    #  we are providing positional arguments in order for placeholders -> {}



# f-strings : formatting when variables will be provided in curly brackets{}

name = "Aashish"                           # 'name' is the variable for placeholder
Place = "India"
print(f"Hey my name is {name} and I am from {Place}")

price = 49
print(f"Your daily wage for this work is ${price}")

print(f"{2 * 30}")             # this (2*30) result is coming in the form of string

name = "Aashish"
print(f"Hey hello {name}")       # printing the 'name' variable's value
print(f"Hey hello {{name}}")     # printing the 'name' variable as it is  using {{}} 
print(f"Hey hello {{{name}}}")   # printing the 'name' variable value in single curly brackets {} 