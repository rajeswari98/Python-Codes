#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def compareStrings(s1, s2):
    # Write your code here
    q = []
    for i in range(len(s1)):
        if s1[i] != '#':
            q.append(s1[i])
        elif len(q) != 0:
            q.pop()
    
    res = ""
    while len(q) != 0:
        res += q[0]
        q.pop(0)
        
    # print(res)
    
    x=[]
    for i in range(len(s2)):
        if s2[i] != '#':
            x.append(s2[i])
        elif len(x) != 0:
            x.pop()
    
    
    res2 = ""
    while len(x) != 0:
        res2 += x[0]
        x.pop(0)
    
    if res == res2:
        return 1
    else:
        return 0

# compareStrings(s1, s2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = compareStrings(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
