# list of vowels
vowelList = ['a', 'e', 'i', 'o', 'u']
str = input()  # education


def vowelsFunction(str):
    length = len(str)
    empt = []
    for i in range(0, length-1):
        if str[i] in vowelList:
            empt.append(str[i])

    s = set(empt)
    convtList = list(s)
    if len(convtList) == 5:
        return True
    else:
        return False


print(vowelsFunction(str))
