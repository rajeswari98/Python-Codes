# s="How are you? I am FINE"
arr=[i for i in input().split(" ")]
print(arr)
upper=[]
for i in arr:
    if i[0].isupper():
        print(i,end=" ")
        upper.append(i)

if not upper:
    print(-1)

    

'''
Words Starting with Upper Case
The program must accept a string S containing multiple words as the input. The program must print the words starting with an upper case alphabet in S as the output. If there is no such word, the program must print -1 as the output.

Boundary Condition(s):
3 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the words starting with an upper case alphabet in S or -1.

Example Input/Output 1:
Input:
How are you? I am FINE

Output:
How I FINE

Explanation:
The words starting with an upper case alphabet are How, I and FINE.
Hence the output is How I FINE

Example Input/Output 2:
Input:
Cricket Match 1: India vs Pakistan

Output:
Cricket Match India Pakistan

Example Input/Output 3:
Input:
hi dora, is this your map?

Output:
-1
'''