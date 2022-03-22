def sumElements(*n):
    total = 0
    for i in n:
        total +=i
    print(total)
    if total%3 == 0:
        return True
    else:
        return False

res = sumElements(2,3,4)
print(res)