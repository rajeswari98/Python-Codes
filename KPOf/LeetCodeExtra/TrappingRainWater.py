# https://leetcode.com/problems/trapping-rain-water/
def TrappingRainWater(l):
    i=1
    j=len(l)-1
    if len(l)<=2:
        return 0
    lmax = l[0]
    rmax = l[-1]
    res=0
    while i<=j:
        if l[i]>lmax:
            lmax = l[i]
        if l[j]>rmax:
            rmax = l[j]
        print(lmax, rmax)
        if lmax<=rmax:
            res += lmax - l[i]
            i += 1
        else:
            res += rmax - l[j]
            j -= 1
    return res
l=[0,1,0,2,1,0,1,3,2,1,2,1]
res=TrappingRainWater(l)
print(res)