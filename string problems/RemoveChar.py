# Python program to remove character from string
'''
For Example:

Input String: Quescol

Input Character : e

Output: Quscol (After removing ‘e’)
'''

str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," ")) 


'''
# Using replace() method 

def remove_char(s1,s2):
    print(s1.replace(s2, ''))

s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 
'''

'''
# Remove character from string using translate() method in python

def remove_char(s1,s2):
    dict = {ord(s2) : None}
    print(s1.translate(dict))

s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 
'''