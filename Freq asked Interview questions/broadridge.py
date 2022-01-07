'''
#read a text file and import into the database 
import pandas as pd

df = pd.read_csv("filename")
#database schema will be
Products name,category, price, status()

#join and split functions
s="thi ss s astring"
split = ['this', 's', 's', 'astring']
print(' '.join(split))
   
#diff with *args and **kwargs
#*args

*args is a special syntax used in the function definition to pass variable-length arguments.
“*” means variable length and “args” is the name used by convention. You can use any other.
def multiply(a, b, *argv):
   mul = a * b
   for num in argv:
       mul *= num
   return mul
print(multiply(1, 2, 3, 4, 5)) #output: 120
**kwargs

**kwargs is a special syntax used in the function definition to pass variable-length keyworded arguments.
Here, also, “kwargs” is used just by convention. You can use any other name.
Keyworded argument means a variable that has a name when passed to a function.
It is actually a dictionary of the variable names and its value.
def tellArguments(**kwargs):
   for key, value in kwargs.items():
       print(key + ": " + value)
tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")
#output:
# arg1: argument 1
# arg2: argument 2
# arg3: argument 3 
def fun(*args):

#-2 negative index in the array
a = [1,2,6]
print(a[-2])

#traverse via function
def get_value(a,i):
	
#oops concept question
class animal
class dog
class cat


'''

#round 2
l = ['a', 'b', 'c']
# method1
print(l[::-1])
#method2
print(list(reversed(l)))
#method3
s= ''
for i in l:
    s = i + s
print(s)


def f():
    for i in l:
        if i == 'b':
        # print(i)
            
            return i
k = f()
print(k)
    

'''
round 3
employee: name, id
employee details : id, age, address
select e.name, ed.address from employee a, employee_details ed join a.id = ed.id where ed.age>=25; 

database: orcale, 

models.py
employee, employee_details
def employee(models.Model):
	name = models.Charfield(max_length=20)
	id = models.Interfield(max_length =10)
def employee_details(models.Model):
	address = models.Charfield(max_length=20)
	id = models.Interfield(max_length =10)
	name = models.Charfield(max_length=20)
	age = models.Interfield(max_length =10)

python manage.py makemigrations
python manage.py migrate

views.py
import . models
def employee(request):
	if request.method == "POST":
		name = employee.objects.get(name)
	if name in employee.models:
		print("Data exists")
	else:
		
		


'''