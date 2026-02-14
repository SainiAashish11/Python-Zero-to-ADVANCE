# dictionaries : These are the ordered key- value pairs 

employee_names = { "Name1" : "Rahul" , "Name2"   : "Sumit"}
employee_id    = { 'ID1'   :   2001    ,  'ID2'    :   2003 }
print(employee_names)                                           # printing all key-value pairs in 'employee_names' dictionary
print(employee_id)                                              # printing all key-value pairs in 'employee_id' dictionary
print(employee_names["Name1"] ,",", employee_id['ID1'])         # accessing different dictionary values via argument passing

# printing with 'f-string'

print(f"The name of the employee is {employee_names['Name2']} with employee id {employee_id['ID2']}")

'''
 Note : for accessing the key-value pair in dictionary , same 'object' should be used
 Example : data = { "name" : "aashish" , "house number" : 24 }
            print(data["name"] , data["house number"])
                      --------       ----------------
'''

# .get() : This doesn't show error when accessed key-value pair is not present in the dictionary

print(employee_id.get('ID3'))   # as 'ID3' is not in the dictionary hence printing 'none'
print(employee_id.get('ID2'))

# accessing multiple values by '.keys()' and '.values()'

print(employee_names.keys())               # accessing all 'keys' only
print(employee_names.values())             # accessing all 'values' for particular 'key'


# for loop
employee_names = { "Name1" : "Rahul" , "Name2"   : "Sumit"}
employee_id    = { 'ID1'   :   2001    ,  'ID2'    :   2003 }

for key in employee_names.keys():          # for loop is traversing on all the 'keys' present in the dictionary         
    print(employee_names[key])             # printing the 'values' for a particular 'key'

for value in employee_names.values():      # for loop is traversing on all the 'values' present in the dictionary
    print(value)                           # printing all the values present in the dictioanry

# .items() for accessing all the 'keys' and 'values' of the dictionary
# accessing both 'keys' and 'values' at a time with single loop
employee_names = { "Name1" : "Rahul" , "Name2"   : "Sumit"}
employee_id    = { 'ID1'   :   2001    ,  'ID2'    :   2003 }

for key , value in employee_names.items() and employee_id.items():      # here, first dictionary is not empty hence for loop is traversing through the second dictionary's 'keys' and 'values'
    print(key , value)


# itertools module : it can traverse the for loop over multiple dictionaries
import itertools

employee_names = {"Name1": "Rahul", "Name2": "Sumit"}
employee_id = {'ID1': 2001, 'ID2': 2003}

# Chain the .items() from both dictionaries together
for key, value in itertools.chain(employee_names.items(), employee_id.items()):
    print(key, value)