#SELF Meaning
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# Note:
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

#Example

class Person:
    def __init__(mysillyobject, name, empid):
        mysillyobject.name = name
        mysillyobject.empid = empid
    
    def myfunc(abc):
        print("My name is "+ abc.name)
    
    def myfunEmp(id):
        print("Empid is " + str(id.empid))

p1 = Person("Rajesh", 111)
p1.myfunc()
p1.myfunEmp()