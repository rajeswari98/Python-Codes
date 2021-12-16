#create a generator function without using range
#what is generator?
'''
Python generators are a simple way of creating iterators. A generator is a function that returns an object (iterator) which we can iterate over (one value at a time)
'''
#what is Ajax?
'''
AJAX = Asynchronous JavaScript And XML.
AJAX is not a programming language.
AJAX just uses a combination of:
    A browser built-in XMLHttpRequest object (to request data from a web server)
    JavaScript and HTML DOM (to display or use the data)
'''
#what is a lookup pair in django?

def gen_fun(start,end , sep):
   
    k=0
    while start<= end:

        k=start
        start = start + sep
        yield(k)

start = 1
end = 8
stop = 2

a=   gen_fun(start, end, stop)


print(next(a))
print(next(a))
print(next(a))
print(next(a))
    
