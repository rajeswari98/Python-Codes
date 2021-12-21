'''
Generators:
    Generators are iterators which can execute only once.
    It uses Yield Keyword.
    It is used mostly in loops to generate an iterator vy returning all the values in the loop without effecting the iteration of the loop.
    Every genertor is an Iterator. Simply It is a subset of Iterators.

Iterator:
    An Iterator is an object which contains a countable number of values. It is used to iterator over iteratable objects like lists, tuple, dict etc..
    Iterators are mostly used to iterate or convert other objects to an iterator using iter() function.
    Iterator uses iter() and next() functions.
    Every iterator is not a generator.
'''

#Generator
print("This is a example for Generator")
def sqr(n):
    for i in range(1, n+1):
        yield i*i
a = sqr(3)

print(next(a))
print(next(a))
print(next(a))

#Iterator
print("This is a example for Iterator")
iter_list = iter(['A', 'B', 'C'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
