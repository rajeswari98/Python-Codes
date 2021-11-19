s1=input().strip()
s2 = input().strip()


for j in s2:
    if j not in s1:
        print(j, end='')
print()

for i in s1:
    if i not in s2:
        print(i, end='')


'''

d = input().strip()
s2 = input().strip()
a, b = [], []
for i in d:
    if i not in a:
        a.append(i)
for i in s2:
    if i not in b:
        b.append(i)
for i in b:
    if i not in d:
        print(i, end="")
print()
for i in a:
    if i not in b:
        print(i, end="")
'''




'''
Uncommon Alphabets
The program must accept values of two string S1 and S2 as input. The program must print the uncommon alphabets in both S1 and S2.

Boundary Condition(s):
1 <= Length of string S1 and S2 <= 1000

Input Format:
The first line contains the value of string S1.
The second line contains the value of string S2.

Output Format:
The first line contains the uncommon alphabet(s) in S2.
The second line contains the uncommon alphabet(s) in S1.

Example Input/Output 1:
Input:
apple
pen

Output:
n
al

Explanation:
n is an uncommon alphabet in pen. So, n is printed
a and l are uncommon alphabets in apple. So, al is printed

Example Input/Output 2:
Input:
hello
world

Output:
wrd
he

'''