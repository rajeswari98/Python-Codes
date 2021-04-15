# A series like question from which you need to guess the given position number.
# 0, 0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, #23, 26, 25, 28, 27, 30, 29, 32, 31, 34, 33, 36, 35, 38, 37, 40, 39, 42, 41, 44, 43, 46, #45, 48, 47, 50
# num = 5(place)---> print 4

el = []
ol = []
n = int(input())
for i in range(99999):
    if i % 2 == 0:
        el.append(i)
    else:
        ol.append(i)
print(el, ol)
el.pop(0)

cl = [0, 0]
t = 0
p = 0
ad = len(el)+len(ol)
for i in range(ad):
    if i % 2 == 0:
        cl.append(el[t])
        t = t+1
    else:
        cl.append(ol[p])
        p = p+1
print(cl)
print(cl[n])
