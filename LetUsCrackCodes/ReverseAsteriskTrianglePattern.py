num=int(input())
for i in range(0,num-1):
    for j in range(num-i-1,0,-1):
        print("*",end='')
    p=i+1
    for n in range(num-i-1,num):
        print(p,end='')
        p-=1
    print()


'''
n=int(input())
for i in range(n):
   print('*'*(n-i-1),end='')
   for j in range(i+1,0,-1):
       print(j,end='')
   print()
'''

'''

Reverse Asterisk Triangle Pattern: The program must accept an integer N as input and print the pattern as given in the Example Input/Output Section.

Boundary Condition(s):
3 <= N <= 50

Input Format:
The first line contains the value of N.

Output Format:
The first N*N lines contain the desired pattern.

Example Input/Output 1:
Input:
5

Output:
****1
***21
**321
*4321
54321

Example Input/Output 2:
Input:
3

Output:
**1
*21
321

Reverse Asterisk Triangle number Pattern program in python
'''
