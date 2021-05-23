'''
num = int(input())
if num < 2:
    print(0)
else:
    prime = [2]
    counter = 3
    while counter <= num:
        for i in range(3, counter, 2):
            if counter % i == 0:
                counter = counter+2
                break
        else:
            prime.append(counter)
            counter = counter+2
    print(prime)
'''
nums = [3, 2, 3]
target = 6
h = {}
for i, num in enumerate(nums):
    n = target-num
    print(h)
    if n not in h:
        h[num] = i
        print(h[num], i)
    else:
        print(h[n], i)
