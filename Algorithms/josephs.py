# Python code for Josephus Problem

def josephus(n, k):

    if (n == 1):
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus(n - 1, k) + k-1) % n + 1

# Driver Program to test above function


n = 14
k = 20

print("The chosen place is ", josephus(n, k))

# This code is contributed by
# Sumit Sadhakar
# another way is convert into binary number and put the first term of the binary number to the last and convert #to decimal
