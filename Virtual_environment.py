''' 
Virtual Environment : Tool to isolate specific Python environments on a single machine, allowing you to work
                      on multiple projects with different dependencies and package without conflicts. This can be especillay useful when
                      working on projects that have conflicting package version or packages that are not compatible with each other
'''

# Command for creating a virtual environment inside 'command propmp' window not PowerShell window :
    # python -m venv myenv
''' Run this command only inside the valid folder location'''

# command for Activating the virtual environment :
    # myenv\Scripts\activate.bat

# command installing the 'libraries and packages' using:
    # pip3 install package_name

# command for deactivating the environment :
    # deactivate

''' Note : After deactivating the virtual environment, global python base interpreter will be used '''


''' Creating a new file for getting details of all the packages installed '''
# command to create a new file into the virtual environment folder
    # touch fil_name.py

# command to see the packages installed in the environment
    # pip freeze 

# command to make a 'txt' file for printing all the packages used in the environment
    # pip freeze > requirements.txt

# command for downloading all the packages from the '.txt' file
    # pip install -r file_name.txt 