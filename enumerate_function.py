'''
Enumerate function : Built-in function that allows us to loop over a sequence (list , tuple , set , string , etc) 
and get the 'index' and 'value' of each element in the sequence at the same time
'''

# Example - 1 ( simple way )
fruits = ["Apple" , "Banana" , "Grapes"]

for index , fruit in enumerate(fruits):   # 'index' and 'fruit' variables are pointing at the same value in the 'list' at the same time
    print(index, fruit)



# Example - 2
marks = (12 , 22 , 97 , 56 , 99 , 0)

for index , mark in enumerate(marks):   # first 'variable' always gives 'index' of the value
    print(mark)
    if( mark == 99 ):
        print("Congratulations on getting higher marks :" , mark)



# Example - 3 ( unpacked tuple )
age = [ 22 , 33 , 44 , 55]

for i in enumerate(age):     # 'i' is the 'tuple' consists of (index , value) 
    print(i)



# Example - 4 ( locating 'index' to a specific value )
age = [ 22 , 33 , 44 , 55]

for i , value in enumerate(age , start = 1):     # index 'i' now starts from '1'
    print(i , value)



# Example - 5 ( string value )
name = "Aashish"

for index , char in enumerate(name):
    print(index , char)