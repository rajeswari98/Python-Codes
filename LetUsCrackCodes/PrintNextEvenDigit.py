num = list(input())
l = []
for n in num:
    k = int(n)
    if(k >= 8):
        l.append('0')
    if(k % 2 != 0 and k != 9):
        l.append(k+1)
    elif(k % 2 == 0 and k != 8):
        l.append(k+2)
print(*l, sep='')


'''
l=list(input())
k=[]
for i in l:
    if i=='8':
        k.append(0)
    elif int(i)%2==0 and i!='8':
        k.append(int(i)+2)
    else:
        if i=='9':
            k.append(0)
        elif i!='9':
            k.append(int(i)+1)
for i in k:
    print(i,end="")
'''

'''
Given a number N, the program must print the next even digit for each of the digits in N,

Boundary Condition(s):
1 <= N <= 999999999

Input Format:
The first line contains N.

Output Format:
The first line contains the specified output.

Example Input/Output 1:
Input:
123

Output:
244

Example Input/Output 2:
Input:
789

Output:
800
'''
