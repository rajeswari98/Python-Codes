s=input()
n=int(input())

if s[:n] ==s[len(s)-n:]:
    print("YES")
else:
    print("NO")

# s=input()
# n=int(input())

# if s[:n] ==s[-n:]:
#     print("YES")
# else:
#     print("NO")

'''
First & Last K – Equal or Not
The program must accept a string S and an integer K as the input. The program must print YES if the first K characters are equal to the last K characters in S. Else the program must print NO as the output.

Boundary Condition(s):
1 <= K <= Length of S <= 100

Input Format:
The first line contains S.
The second line contains K.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
marksmar
3

Output:
YES

Explanation:
The first 3 characters in marksmar are m, a and r.
The last 3 characters in marksmar are m, a and r.
Here the first 3 characters are equal to the last 3 characters in marksmar.
Hence the output is YES

Example Input/Output 2:
Input:
ring
4

Output:
YES

Example Input/Output 3:
Input:
letuscrackletu
6

Output:
NO

'''