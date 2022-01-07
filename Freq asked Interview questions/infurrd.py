#String reverse
# l = [i for i in range(0,10)]
# print(l)
# print(l[::-3])

#Fibonacci Series starting from 1
num = int(input())
num1 = 1
num2 = 1
count = 0
if num == 1:
    print(num1)
else:
    while count < num:
        temp = num1 + num2
        num1 = num2
        num2 = temp
        
        count = count +1
        print(num1)
    
    