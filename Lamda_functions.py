# Lamda Function : It is a small anonymous function without name
# It is defined using the 'lamda' keyword

# Syntax : function_name = lambda variable : variable_expression


# Examples - 1
division = lambda x: x / 2
print(division(2))

cube = lambda x: x*x*x
print(cube(3))


# Example - 2
# multiple variables in lambda expression
avg = lambda x , y , z: (x + y + z) /3
print(avg(2 , 3 , 4))


# Example - 3
# use of lambda function in a function
cube = lambda x: x * x * x    # cube as lambda function

def sum(fx , value):          # function for calculating the sum
    return 6 + fx(value)

print(sum(cube , 2))          # 'avg function' is calling 'cube lambda function' and 'value = 2'


# Note : Lambda function are used as arguments in higher order functions like map , filter and reduce