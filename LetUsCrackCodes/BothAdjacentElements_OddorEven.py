num=int(input())
l=list(map(int,input().split()))[:num]
for n in range(1,num-1):
    if( (l[n-1]%2!=0 and l[n+1]%2!=0) or (l[n-1]%2==0 and l[n+1]%2==0)):
        print(l[n],end=' ') 
    

'''
Both Adjacent Elements – Odd or Even: Given an array of N positive integers, print the positive integers that have both the adjacent element values as odd or even.

Boundary Condition(s):
3 <= N <= 1000

Input Format:
The first line contains N.
The second line contains N elements separated by space(s).

Output Format:
The first line contains the elements (which have both the adjacent element values as odd or even) separated by a space.

xample Input/Output 1:
Input:
7
10 21 20 33 98 66 29

Output:
21 20 33

Example Input/Output 2:
Input:
5
11 21 30 99 52

Output:
30 99
'''