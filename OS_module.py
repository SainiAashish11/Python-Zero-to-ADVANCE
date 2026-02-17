'''
    OS Module in python is a built-in library that provides functions for interacting
    with the 'operating sytem'. It allows us to perform a wide variety of tasks, such as
    reading and writing files, interacting with the file system, and running system commands
'''
# Note : Don't run any command here because already a folder named 'OS_module' exists for these operations and it's results
# Note : All the codes are valid for 'OS_module' folder


# creating a folder
import os 
if not (os.path.exists):  # checking if the folder already exists or not
    os.mkdir("Data")      # os.mkdir("") for creating a new folder    

# creating multiple folders inside the folder
for i in range (1,11):
    os.mkdir(f"Data/Day{i}")     # f-string for writing the name of the folder



# for changing the name of the folder
import os
for i in range(1,11):
    os.rename(f"Data/Day{i}" , f"Data/Tutorial{i}")    # os.rename( source_name , Destination_name )



# listing all the folders present inside the main folder
import os
folders = os.listdir("OS_module")
print(folders)



# checking the files present inside the folders of the main folder
for folder in folders:
    print(folder)
    print(os.listdir(f"OS_module/{folder}"))



# running a command into the command prompt
import os
cmd = 'date'
os.system(cmd)



# telling the current directory
import os
print(os.getcwd())



# change the directory
os.chdir("/Users")
print(os.getcwd())



# deleting a file
import os
os.remove("")   # removes a file
os.rmdir("")    # removes an empty directory