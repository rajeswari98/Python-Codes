MainString=list(input().strip())
string=[]
for i in MainString:
    if i not in 'aeiouAEIOU':string.append(i)
lenCon=len(string)
revString=string[::-1]
#print(string,revString)
v=0;b=0
for i in range(lenCon):
    if i%2==0:
        print(string[v],end='')
        v+=1
    else:
        print(revString[b],end='')
        b+=1

'''
n=input()
m='aeiouAEIOU'
b=''
v=0
x=0
for i in n:
    if i not in m:
        b+=i 
c=b[::-1]
for i in range(len(b)):
    if i%2==0:
        print(b[v],end='')
        v+=1 
    else:
        print(c[x],end="")
        x+=1
'''

'''
Consonants from Start End Alternate: A string S is passed as the input to the program. The program must print the consonants from the start position and the consonants from the end position alternatively. No character at the same position in the string must be printed twice.

Boundary Condition(s):
1 <= Length of String S <= 1000
Input Format:
The first line contains the value of S

Output Format:
The first line contains the consonants in S printed based on the above conditions.

Example Input/Output 1:
Input:
machine

Output:
mnch

Example Input/Output 2:
Input:
environment

Output:
ntvnrmn
'''