num = input()
firstTwo = num[0:2]
lastTwo = num[-2:]
print("yes" if firstTwo == lastTwo else "no")


'''
#check string in first and last two digits and 
# print “yes” if the first two digits and the last two digits are same, otherwise print “no”.
num=input()
l=[]
for i in range(len(num)):
    l.append(num[i])

firstTwo=l[0:2]
lastTwo=l[-2:]
str1=''.join(firstTwo)
str2=''.join(lastTwo)
if str1.isdigit() and str1==str2 and str2.isdigit():
    print("yes")
else:
    print("no")

'''

'''
question:
Check First & Last Two Digits: Accept a number N and print “yes” if the first two digits and the last two digits are same, otherwise print “no”.

Input Format:
The first line contains a number N.

Output Format:
The first line contains the “yes” or “no” based on the above mentioned condition.

Boundary Conditions:
9 <= N <= 9999999

Example Input/Output 1:
Input:
155215

Output:
yes

Example Input/Output 2:
Input:
9217623

Output:
no
'''
