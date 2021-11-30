# Print the sum of the digits
# num = input()
# sum=0
# for i in str(num):
#     sum = sum+ int(i)
# print(sum)


# reverse a string
# name=input()
# print(name[::-1])
# print(list(reversed(name)))


# n=1 Cap, 1 small, 1 num, 1 special

special_char = ['@', '$','#']
# Pwd = input()
small_letters =[chr(i) for i in range(ord('a'),ord('z')+1)]
cap_letters = [chr(i) for i in range(ord('A'),ord('Z')+1)]
nums=['0','1','2','3','4','5','6','7','8','9']

# for i in range(len(Pwd)):
#     if Pwd[i] in special_char and Pwd[i] in small_letters  and   Pwd[i] in cap_letters and Pwd[i] in num:
#         print("true")

#max length of the password is 6

import random
import array
rand_digit = random.choice(nums)
rand_uppercase = random.choice(cap_letters)
rand_lowercase = random.choice(small_letters)
rand_sym = random.choice(special_char)

temp_pass = rand_digit+ rand_lowercase + rand_uppercase + rand_sym
Max_Len = 6

#filing the remaiaining space with the random combinations
combined_list = nums + small_letters + cap_letters + special_char
for i in range(Max_Len-4):
    temp_pass = temp_pass + random.choice(combined_list)
    #convert temp pass into array and shuffle
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ''
for x in temp_pass_list:
    password = password + x

print(password)



