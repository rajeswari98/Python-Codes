from itertools import permutations as p
s1=input()
s2=input()
for i in range(len(s1)+1):
    for j in list(p(s1,i)):
        if ''.join(j)==s2:
            print("YES")
            exit()
print("NO")




'''

The program must accept two integers M and N as input. The program must print “YES” if an integer N is formed from the digits of M. Else the program must print “NO” as the output.

Boundary Condition(s):
1 <= M, N <= 999999999

Input Format:
The first line contains the value of M.
The second line contains the value of N.

Output Format:
The first line contains “YES” or “NO“.

Example Input/Output 1:
Input:
12345
45321

Output:
YES

Example Input/Output 2:
Input:
5555 
65

Output:
NO
'''



