# #[-5, -23, 5, 0, 23, -6, 23, 67]
# #-23, -6, -5, 0, 5, 23, 23, 67]
#list sorting without sort function
# l = [1,2,0,0,0,1,1,-1]


# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] > l[j]:
#             temp = l[i]
#             l[i] = l[j]
#             l[j] = temp
            
# print(l)

#decorator
# def dec_fun(name):
#     if name == "some":
#         return True
#     else:
#         return False
        


# @dec_fun(name)
# def fun(name):
#     return name

# print(fun(input()))
# a=3
# print(a)
# def fun():
#     a=10
#     print(a)
# print(fun())

# private variables demo
# class fun:
    
#     def name:
#         a=10
#         return a
        
    
# a = fun()
# print(a.name)

#Did you use any multi threading inside the project?

    




# round  2
# def sum1(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# a=3
# b=2
# sum_updated = sum1(a,b)
# @sum1(a,b)
# def ex(sum1, diff):
#     print(sum1, diff)

# # 'output of a and b is : '
# def 

def generate(l):
    for i in range(l):
        yield i
   

l=3
x = generate(l)
print(next(x))
print(next(x))
print(next(x))

'''

django-admin startproject 

empid, salary

models.py
def employee(models.Model):
    empid = models.CharField()
    Salary = models.NumericField()
    EMPSTATE = MODELS.CHARFIELD(NULL=True)
    UNIVERSITY = MODELS.CHARFIELD()



def example(models.Model):
    order = models.ForeignKey(employee, on_delete=models.CASCADE,)

PYTHON MANAGE.PY SHELL
python manage.py makemigrations
python manage.py migrate

FORM
{{SALARY}}

def employee(request.get['empid'], request.get['salary']):

    return render('templateName', {empid, salary })

'''