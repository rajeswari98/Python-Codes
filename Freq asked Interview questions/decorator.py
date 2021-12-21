#Decorator
#A decorator is just a function which takes another function as an argument and add some
#kind of functionality and return another function without making changes to the existing function

def dec_fun(func):
    def wrap_func():
        print("Inside the wrap function")
        return func()
    
    print("Inside the dec_function")
    return wrap_func

def show():
    print("This is a starting point!")

dec_show = dec_fun(show)
dec_show()


#alternative
@dec_fun
def display():
    print("This is a display function!")
display()

'''
def decorator_lowercase(function):   # defining python decorator
def wrapper():
func = function()
input_lowercase = func.lower()
return input_lowercase
return wrapper
@decorator_lowercase    ##calling decoractor
def intro():                        #Normal function
return 'Hello,I AM SAM'
hello()
'''