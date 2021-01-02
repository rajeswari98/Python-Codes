s=input().strip()
underscoreList=[]
for i in range(len(s)-1):
    if s[i]=='_':
        underscoreList.append(i)
#print(underscoreList)
print(s[0:underscoreList[0]]+'_',end='')
for i in range(len(underscoreList)-1):
    print(s[underscoreList[i]+1:underscoreList[i+1]][::-1]+'_',end='')
print(s[underscoreList[-1]+1:])


'''
s= input().strip()
l=[]
for i in range(len(s)-1):
    if s[i]=='_':
        l.append(i)
print(l)
print(s[0:l[0]]+'_',end='')
for i in range(len(l)-1):
    print( s[l[i]+1:l[i+1]][::-1] +'_',end='')
print(l[-1]+1)
print(s[l[-1]+1:])
'''

'''
Reverse the Substrings Between Underscores: String S is passed as the input. The String S may have zero or more underscores in it. The program must reverse the substrings between the underscore in S. 

Boundary Condition(s):
Length of the S from 3 to 100.


 
Input Format:
The first line contains the string S with substrings between underscores reversed.

Output Format:
The first line contains the string S modified based on the given conditions.

Example Input/Output 1:
Input:
abcd_efgh_ijke_mnl

Output:
abcd_hgfe_ekji_mnl

Example Input/Output 2:
Input:
_apple_mango

Output:
_elppa_mango
'''