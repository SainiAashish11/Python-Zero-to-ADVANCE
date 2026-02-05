print("hello world")    # "hello world" is a string object  which should be quoted inside the double or single quotations
print(5)                #  5 is a number which shouldn't be quoted
print('bye', ',' ,7)   # by using comma(,) we are printing objects of different types
print(12*12)            # * used for multiplication
print(12/12)            # / used for division
print(12+12)            # + used for addition
print(12-12)            # - used for substraction

# python interpreter running the code line by line from top to bottom and if there is any error at any point then it will only output before the error
# (ctrl + /) used for comment or uncomment the selected lines
# comments are used for not executing the commented lines of code or used only for explanation of code

'''
hello world, i am learning python for the first time                                 
and its kinda interesting and easy for first hands on experience

'''                                                                                   # multi line comment by triple single or triple double quotes            

print("i am studying in IIIT dharwad \n and it is an average college in India ")      # Here '\n'  is an escape sequence character used for 'new line'

print("hey there is a way \'and\' i am going there")                                  # \" anything written \" or \' anything written\' shows output in respective quotes

print("hello" , 27 , 11 , sep = "~")                                                  # sep="any character"  is used to separate the objects inside the print function with this separator

print("hello" , 27 , 11 , end="~!@#$%^&*()_+")                                        # end=" "  is used to end the object with given character or number with end operator