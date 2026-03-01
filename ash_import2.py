def Welcome():
    print("you are welcome my dear friend")

name = "Aashish"

print(__name__)               # it results in '__main__' string if this script is executed, means '__main__' is also present in this script
if __name__ == "__main__":
    Welcome()

''' __name__ is a built-in variable which tells the name of the script if 'import' happened
    otherwise prints the string '__main__' if executed from the same script, like her '__name__' and '__main__' are present in same script
'''

# 'if' checks whether the '__name__' variable is running in the same script or in the other script where it is imported
# always check the functionality of the code if we are importing the script into our new script for unwanted events
