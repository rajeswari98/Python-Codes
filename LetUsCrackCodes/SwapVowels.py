string1 = list(input().strip())
l1 = []
l2 = []
string2 = list(input().strip())
x = 0
y = 0

vow = ['a', 'e', 'i', 'o', 'u']
for i in range(len(string1)):
    if string1[i] in vow:
        l1.append(string1[i])
for i in range(len(string2)):
    if string2[i] in vow:
        l2.append(string2[i])

# print(string1,string2,l1,l2)

k = min(len(l1), len(l2))
for i in range(len(string1)):
    if string1[i] in vow and x < k:
        string1[i] = l2[x]
        x += 1
    print(string1[i], end='')
print()
for j in range(len(string2)):
    if string2[j] in vow and y < k:
        string2[j] = l1[y]
        y += 1
    print(string2[j], end='')



'''
optimized way

string1=list(input().strip());l1=[];l2=[]
string2=list(input().strip());x=0;y=0;vow=['a','e','i','o','u']
for i in range(len(string1)):
    if string1[i] in vow:l1.append(string1[i])
for i in range(len(string2)):
    if string2[i] in vow:l2.append(string2[i])
#print(string1,string2,l1,l2)

k=min(len(l1),len(l2))
for i in range(len(string1)):
    if string1[i] in vow and x<k:string1[i]=l2[x];x+=1
    print(string1[i],end='')
print()
for j in range(len(string2)):
    if string2[j] in vow and y<k:string2[j]=l1[y];y+=1
    print(string2[j],end='')
'''


'''
Two Strings – Swap Vowels: The program must accept two string values S1 and S2 as the input. The program must swap vowels in the first string with vowels in the second string in the order of their occurrences. Then the program must print the modified string values as the output.

Boundary Condition(s):
1 <= Length of S1 and S2 <= 1000
Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains modified S1.
The second line contains modified S2.

Example Input/Output 1:
Input:
environment
auditorium

Output:
anvurinmont
eidoterium

Explanation:
The vowels in the first string (environment) in the given order are e, i, o and e.
The vowels in the second string (auditorium) in the given order are a, u, i, o, i and u.

 

These vowels are swapped in both the string values in the given order.
So the two string values become anvurinmont and eidoterium.
The string S2 has two vowels more than the string S1 which are not swapped.

Example Input/Output 2:
Input:
pen
basket

Output:
pan
besket
'''
