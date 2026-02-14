# update() : To update the current dictionary

info1 = {'name' : 'Rohit' , 'age' : 21}
print(info1)
info1.update({'DOB' : 2002})
info1.update({'occupation' : 'Businessmen'})
print(info1)

# updating one dictionary with another dictioanry data

info2 = {'work_exp(in yrs)' : 2 , 'job_role' : 'SDE' , 'Language' : 'English'  }
info1.update(info2)
print(info1)

print(info1.update())
# Note : update() method returns 'none' if 'no' argument is present


# clear() : It clears all the data and returns the 'empty dictionary'

info1.clear()
print(info1)


# pop() : It removes the given key-value pair from the dictionary

info2 = {'work_exp(in yrs)' : 2 , 'job_role' : 'SDE' , 'Language' : 'English'  }
info2.pop('job_role')
print(info2)

# popitem() : It removes the last item from the dictionary

House_no = {122 : "Aashish Saini" , 111 : "Rahul Saxena" , 121 : "Biswas Jindal"}
House_no.popitem()
print(House_no)


# del : It deletes the item if 'key' is given otherwise deletes the whole dictionary
info2 = {'work_exp(in yrs)' : 2 , 'job_role' : 'SDE' , 'Language' : 'English'  }
del info2['work_exp(in yrs)'] 
print(info2)
