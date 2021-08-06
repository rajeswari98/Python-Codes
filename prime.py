num=int(input("Enter any number:"))
def prime_numbers(num):
    if num<2:
        return 0
    counter=3
    prime=[2]
    while (counter<=num):
        for i in range(3,counter,2):
            if counter%i==0:
                counter=counter+2
                break
        else:
            prime.append(counter)
            counter=counter+2
    print(prime)
    return len(prime)

print(prime_numbers(num))

'''
num=int(input())
c=3
if(num==0):
    print("Please enter a positive number")
elif num==1:
    print("{} is not a prime number".format(num))
elif num==2:
    print("{} is not a prime number".format(num))
else:
    while(c<=num):
            for i in range(3,num,2):
                temp=1
                if c%i==0:  
                    c+=2
                    temp=0
                    break    
            else:
                c+=2
                temp=1
    if temp==1:
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))
'''

'''
another way

num = int(input())
if num==0:
    print("enter a positive number")
elif num==1 or num==2:
    print("this is not a prime number")
else:
    prime=[]
    counter=3
    while (counter<=num):
        flag=1
        for i in range(3,counter,2):
            if counter%i==0:
                counter=counter+2
                flag=0
                break
        if flag:
            prime.append(counter)
            counter=counter+2
print(prime)
'''