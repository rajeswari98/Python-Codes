num  = int(input())
l = list(map(int,input().split()))[:num]
c= int(input())
contains_list = []
for i in range(len(l)):
    if str(c) in str(l[i]):
        contains_list.append(int(l[i]))
if contains_list:
    print(sum(contains_list))
else:
    print(-1)

'''
#another approach
N=int(input())
arr=[(i) for i in input().split()]
k=input().strip()
final=[]
for i in arr:
    if k in i:
        final.append(i)
if not final:
    print(-1)
else:
    res=[int(i) for i in final]
    print(sum(final))

'''



'''
Sum – Integers having at least one D
The program must accept N integers and a digit D as the input. The program must print the sum S of integers having at least one D among the N integers. If there is no such integer, the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^7
0 <= D <= 9

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains D.

Output Format:
The first line contains S or -1.

Example Input/Output 1:
Input:
5
445 7891 545 309 154
4

Output:
1144

Explanation:
The integers with at least one 4 are 445, 545 and 154.
So their sum 1144 is printed as the output.

Example Input/Output 2:
Input:
4
999 456 215 328
7

Output:
-1
'''