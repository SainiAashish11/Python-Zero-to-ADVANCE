''' Generators : Python Generators are simple way of creating 'iterators' 
It is a special function which doesn't removes from the memory once executed, but it reminds the values of it's values i.e. 'yield' '''
# Basic Generator code
def gen_demo():

    yield 'First Statement'
    yield 'Second Statement'
    yield 'Third Statement'

gen = gen_demo()     # calling 'gen_demo()' function and result is returning to 'gen' variable, here only 'generator' is created not it's function is called still now
print(gen)           # 'generator object' will be printed with memory address and called here only for printing things


# printing the outputs of 'yield' operator
print(next(gen))
print(next(gen))
print(next(gen))

# trying to print the outputs of 'yield' with 'for loop'
for i in gen():
    print(i)
'''Why doesn't the for loop print anything?
After your three 'next(gen)' calls, the 'generator' is already exhausted.
So when the for i in gen: loop starts:
It tries to pull the 'next value' from the generator.
But since the generator is finished (no more yield left), it immediately ends the loop without printing anything.'''


'''How to fix / see both behaviors
If you want both manual 'next()' calls and a for loop to show results, you need a 'fresh generator' for the loop:'''
for i in gen_demo():      # new generator is created by calling 'gen_demo()' function again and pointing to the memory address of the first 'yield'
    print(i)



''' Yield vs Return 
~ Yield reminds that last time where it has stopped.
~ Return just simply returns the value to the function and vanishes from the memory if not stored in any variable '''


# Range() function implementation using generators
def mera_range(start , end):

    for i in range(start , end):
        yield i                        # yielding every value from start => end


for i in mera_range(15 , 26):         # creating 'generator' and traversing with for loop variable 'i'
    print(i)


''' Generator Expression '''
gen = ( i**2 for i in range(1 , 21))        # creating generator and yielding values as squares 'i**2'
 
for i in gen:
    print(i)



''' Benefits of Generators :
1- Ease of implementation
2- Memory efficient : Generator can load data one by one like iterator , but we are using 'generators' because of it's ease of implementation
3- Representing infinite stream of data
4- Chaining generators
'''

#2- memory efficient example :
L = [ x for x in range(100000)]
gen = ( x for x in range(100000))

import sys
# sizes in bytes
print('Size of List(L) in memory : ' , sys.getsizeof(L))
print('Size of Generator(gen) in memory : ' , sys.getsizeof(gen))

#3- Representing infinite stream of data having 'Positive even' numbers only
def infinite_stream():
    n = 0
    while True:
            yield n
            n += 2 

gen = infinite_stream()     # generator is created here but not yet called

print(next(gen))
print(next(gen))
print(next(gen))


#4- Chaining generators
def fib_series(nums):
    x , y = 0 , 1
    for _ in range(nums):
        x , y = y , x + y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fib_series(10))))