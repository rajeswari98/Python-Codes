# https://leetcode.com/problems/decode-ways/

def numDecodings(s):
    v = 0
    w = int(s>'')
    p=''
    for i in s:
        v,w,p = w, (i>'0')*w + (9<int(p+i)<27)*v, i
    return w
s = "226"
print(numDecodings(s))

#2, 2, 6 --> 1
#22, 6 --> 2
#2, 26 --> 3