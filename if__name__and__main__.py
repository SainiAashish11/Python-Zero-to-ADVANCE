''' If any function or method present in the module that we are importing into our current script 
    then that module will execute it's functions/methods at the time of importing only
'''
# for Example :
import ash_import as a       # it's executing the 'Welcome()' function from 'ash_import' file itself while importing


# if __name__ == "__main__" 
# it used to specify that the given 'function/method' will only be run from the script in which it is written solely not from any other script ( unitll called explicitely )

import ash_import2 as a2     # it's not printing the 'Welcome()' function from 'ash_import2'
a2.Welcome()                 # explicit calling of 'Welcome()' function