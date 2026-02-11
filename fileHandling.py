# method 1 
f = open('myfile.txt' , 'r' )
text = f.read()
print(text)
f.close() 

# Working:
''' 
- f = open('myfile.txt', 'r')
This line opens the file named 'myfile.txt' in read mode ('r'). The file object is assigned to the variable 'f'.

- text = f.read()
The '.read()' method reads the entire content of the file and stores it as a single string in the 'text' variable.

- print(text)
This line prints the string stored in the 'text' variable to the console.

- f.close()
This is a crucial step that closes the file, releasing it from your program's control.

'''

# method 2 - we don't have to close file manually
with open('myfile.txt' , 'r' ) as f:
    file = f.read()
print(file) 

# method 3 - append in text file
with open('myfile.txt' , 'a') as f:
     f.write("hello babes")


# Note : 'method 2' is best for reading a file coz it has automatic file closing facility whether an 'error' is present inside 'with' statement or not
   