st = input()
l = len(st)
firstLt = int(st[0])
p = []
for i in range(1, l):
    p.append(i)
lp = len(p)
if firstLt == lp:
    print("TRUE {}".format(lp))
else:
    print("FALSE {}".format(lp))

"""
inp: 5hello
olp: TRUE 5
"""
