start,end=map(int,input().split())
divNum=int(input())
l=[i for i in range(end,start-1,-1) if i%divNum==0]
k=[j%10 for j in l]
#print(l,k)
for i in range(len(l)):
    print(*[l[i]*k[i]],end=' ')


'''
num=input().split()[0:2]
start=int(num[0])
end=int(num[1])
divNum=int(input())
l=[]
p=[]
for i in range(start,end):
    if i%divNum==0:
        l.append(i)
        p.append(str(i)[-1])
        

k=l[::-1]
h=[]
m=[]
p=p[::-1]
for i in p:
    h.append(int(i))        
print(h)
for i in range(len(k)):
    m.append(h[i]*k[i])
print(*m,sep=' ')
'''


'''

Multiply Multiples with Unit Digit: Two numbers X and Y are passed as the input where Y > X. Another number N is also passed as the input to the program. The program must print the values which are nothing but multiples of N from Y to X (in the reverse order inclusive of Y and X) multiplied with their unit digit.

Boundary Condition(s):
2 <= Y <= 1000000
X < Y
1 <= N <= 100
Input Format:
The first line contains the value of X and Y separated by a space.
The second line contains the value of N.

Output Format:
The first line contains the numerical values as mentioned in the problem statement.

Example Input/Output 1:
Input:
5 25
3

Output:
96 21 144 75 24 81 36

Explanation:
The numbers from 25 to 5 divisible by 3 are 24 21 18 15 12 9 6.
Their unit digits are 4 1 8 5 2 9 and 6 respectively.
So the numbers are 24*4=96, 21*1 = 21, 18*8 = 144, 15*5 = 75, 12*2=24, 9*9 = 81 and 6*6 = 36.
'''