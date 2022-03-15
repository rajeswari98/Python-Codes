
# Print a number pyramid of height n.

# Case A: n=2
#   1
#  222

# Case B: n=3
#     1
#   222
#   33333
#  1
# 222 
#   1
#  222
# 33333

n=5
def py(n):
    
    for j in range(1,n+1):
        for l in range(n-j):
            print(' ',end='')
        k=2*j -1
        
        for k in range(k):
            print(j,end='')
        
        print('')
        

py(n)



