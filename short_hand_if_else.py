# Example - 1
a = 300
b = 3003
print(f"A > B : {a} > {b}") if a > b else print("A < B")
# first print() statement will be printed when uske just aage wala 'if' condition will be 'True' otherwise 'else' will be executed


# Example - 2
c = 9 if a > b else 0
print(c)       # 'c' will become '0' coz value of 'a' is lesser than 'b' above

# Note : Don't use this short hand 'if-else' when logic is complex and large