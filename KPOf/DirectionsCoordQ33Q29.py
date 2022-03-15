s = 'UDDLRL'

def Cor(s):
    U, L, R, D, x, y = 0, 0, 0, 0, 0, 0
    for i in s:
        if i == 'U':
            y += 1
        elif i == 'R':
            x += 1
        elif i == 'L':
            x -= 1
        elif i == 'D':
            y -= 1
        else:
            continue
    return (x,y)
         
print(Cor(s))