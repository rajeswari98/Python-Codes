# num = int(input)
s= input()
k=[s]
# for i in range(num):
#     k.append(input())

aplList=[]
for i in range(ord('a'), ord('z')+1):
    aplList.append(chr(i))
    # print(chr(i))


# for s in k:
l=[]
count=0
Asciicount=0
# for i in range(len(k)):
#     lenI = len(k[i])-1
#     print(i,k[i][lenI])


d={}
for word in range(len(k)): 
    for wordLetter in range(len(k[word])):
        if k[word][wordLetter] in d:
            d[k[word][wordLetter]] += 1
        else:
            d[k[word][wordLetter]] = 1

ASCIICountList=[]
a=False
for word in range(len(k)): 
    for j in range(len(aplList)):
        for wordLetter in range(len(k[word])):
            for key,value in d.items():
                if key == aplList[j]:
                    if d[key] == j+1:
                        a=True
                        print(key, d[key],aplList[j], j+1)
                    else:
                        a=False

                
            # if k[word][wordLetter] == aplList[j]:
            #         Asciicount =  j + 1
            #         ASCIICountList.append(Asciicount)

            #         print(k[word][wordLetter], aplList[j], Asciicount, j, ASCIICountList )

print(d)

dl=[]
for c in d:
    dl.append(d[c])            

print(sum(ASCIICountList), sum(dl))

print(Asciicount)
print(a)









'''
Super ASCII String Checker
The program must accept N string values as the input. For each string S among the N string values, the program must print Yes if it is a super ASCII string. Else the program must print No as the output. A string is said to be a super ASCII string if and only if the count of each character in the string is equal to its super ASCII value. The super ASCII value of ‘a‘ is 1, ‘b‘ is 2, ‘c‘ is 3,… ‘z‘ is 26.
Note: Each string contains only lower case alphabets.

Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string <= 400

Input Format:
The first line contains N.
The next N lines, each containing a string.

Output Format:
The first N lines, each containing Yes or No.

Example Input/Output 1:
Input:
2
abcbcc
dcddd

Output:
Yes
No

Explanation:
In the first string “abcbcc“,
The count of the alphabet ‘a’ is 1. The super ASCII value of ‘a’ is also 1.
The count of the alphabet ‘b’ is 2. The super ASCII value of ‘b’ is also 2.
The count of the alphabet ‘c’ is 3. The super ASCII value of ‘c’ is also 3.
Here the string “abcbcc” is a super ASCII string. So Yes is printed.
In the second string “dcddd“,
The count of the alphabet ‘d’ is 4. The super ASCII value of ‘d’ is also 4.
The count of the alphabet ‘c’ is 1. The super ASCII value of ‘c’ is 3.
Here the string “dcddd” is NOT a super ASCII string. So No is printed.

Example Input/Output 2:
Input:
3
bdcdcd
fafffff
zzzzzzzzzzzzzzzzzzzzzzzzzz

Output:
No
Yes
Yes
'''