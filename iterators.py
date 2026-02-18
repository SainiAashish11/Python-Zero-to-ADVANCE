''' Iteration : General term for taking each item of something one after another. Like a loop is going over on each item in a group of items( list , tuple , set , dictionary , string) '''
''' Iterator  : An object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory '''
''' Iterable  : An object on which one can iterate (list , set , tuple , dictionary , str). It generates an 'iterator' when passed to 'iter()' method by the 'iterable' '''

# Iteration
import sys
L = [x for x in range(1 , 100000)]     # 'range()' is an iterable

for i in L:
    print(i)        # printing every number from list 'L'

print(sys.getsizeof(L) / 64)          # size of list 'L' in 'mb'


# Iterator ( efficient to traverse the data as it doesn't store the whole data in the memory )
import sys
x = range(1 , 100000)            # 'x or range()' function is an iterable here which creates '__iter__' magic method => which produces an 'iterator'

for i in x:                      # here 'range()/x' is iterable which will create 'range_iterator' as '_it = iter(x)' which will create 'next(_it)' and 'i' is the loop variable which will receives the 'current value' from the 'next(_it)' operator
    print(i)
'''Analogy
Think of it like a water tap:
iter(x)       → the tap (produces drops of water one by one).
next(iter(x)) → the water drop that comes out each time.
i             → the bucket where each drop is collected temporarily before you use it.
'''
print(sys.getsizeof(x) / 64)      # size of iterator 'iter(x)' in 'mb'



# Iterable 
L = [ x for x in range(100)]     # 'L' is an iterable 
print(L)
print(iter(L))      # prints the 'iterator' of 'iterable' object

''' Points to remember :
1 - Every Iterator is also an Iterable 
2 - Not all iterables are iterators (Example : When list 'L' as 'iterable' is created, it stored fully in the memory but 'iterators' doesn't store anything completely in once )
'''

''' Trick
1- Every 'iterable' has an 'iter() function 
2- Every iterator has both 'iter() and 'next()' function
'''
a = 2                      # int data type
string = "Hello"           # string data type
lst = [1 , 2 , 3]          # list data type

# printing the whole list of methods that can be performed over these data types
# If only 'iter()' function is present means they are 'iterable' and if 'iter()' and 'next()' both methods are present means it is an 'iterator'
print(dir(a))
print(dir(string))
print(dir(lst))


''' Understanding how for loop works '''
num = [1 , 2 , 3]
for i in num:
    print(i)


# how for loops works in behind
num = [1 , 2 , 3]

# Step-1- fetching the iterator
iter_num = iter(num)      # iter() function making 'iter_num' as an iterator

# Step-2- next() function for knowing the state of iterator => iter_num
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))


''' Making our own For Loop '''
def My_loop(iterable):

    iterator = iter(iterable)        # fetching the 'iterator' from the 'iterable'

    while True:       # infinte loop by using 'True' till the 'except' block will not be executed
        try:
            print(next(iterator))    # printing the state of iterator using 'next(iterator)'
        except StopIteration:
            break

My_loop([1 , 2 , 3])            # passing 'list' as iterable
My_loop(range(1 , 11))          # passing 'range()' function as iterable
My_loop((1 , 2 , 3))            # passing 'tuple' as iterable
My_loop({1 , 2 , 3})            # passing 'set' as iterable
My_loop({0:1 , 1:1 , 2:2})      # passing 'dictionary' as iterable


''' A consfusing point : iterator of iterator '''
num = [1 , 2 , 3]

iter_obj1 = iter(num)
print(id(iter_obj1) , "Address of 1 iterator")

iter_obj2 = iter(iter_obj1)
print(id(iter_obj2) , "Address of 2 iterator")

# Note : Address for both the iterators coming to be 'same' which means the 'iterator obj2' is 'iterator obj1' itself

               
''' Creating our own range() function '''
class Mera_range:
    def __init__(self , start , end):
        self.start = start
        self.end   = end

    def __iter__(self):
        return Mera_range_iterator(self)       # here we are passing the Mera_range(start , end) object to object of 'Mera_range_iterator' class through which iterator object will get the 'start' and 'end' of the 'for loop' to be run
    

class Mera_range_iterator:
    def __init__(self , iterable_obj):     # 'iterable_obj' argument will get 'Mera_range(start , end)' object through which we can access 'start' and 'end' values given in object => Mera_range(start , end)
        self.iterable = iterable_obj       # initialization of 'iterable_obj' in 'self.iterable' so that object of iterator class can access 'start' and 'end' values from 'Mera_range(start , end)' object

    def __iter__(self):         # when iter(iterator) is called it returns itself
        return self
    
    def __next__(self):         # getting

        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start += 1
        return current
        

x = Mera_range(1 , 11)    # object of 'Mera_range' class which is an 'iterable' as 'Mera_range(1 , 11)' then it calls 'x.__iter__()' of it's own class where 'Mera_range_iterator()' object is getting 'Mera_range(1 , 11)' object and stores 'start' and 'end' values of the loop
for i in x:
    print(i)

print(x)                 # printing the address of the 'Mera_range' class's object 
print(iter(x))           # object of 'Mera_range_iterator' class which is an 'iterator'
print(iter(iter(x)))     # 'iterator' of 'iterator' from class 'Mera_range_iterator' by using '__iter__' method


# making 'Mera_range(1 , 11)' object with 'start' and 'end' values which will be used by the iterator 'Mera_range_iterator' and these values will be used in 'Mera_range_iterator' class methods '__iter__' or '__next__'
for i in Mera_range(1 , 11):     # this for loop calls the '__iter__' method from the iterable class i.e. 'Mera_range' and in '__iter__' method => object 'Mera_range_iterator' is returned with Mera_range(start , end) object itself having 'self' as 'self.start' and 'self.end'
    print(i)


''' Application of Iterator Protocol :
We can use this technique as 'memory optimization' in Deep learning where we need to convert our huge amount of image data into 'Numpy' array 
using iterator approach which can load images one by one in the memory which reduces the overall space acquisition '''
