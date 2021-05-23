lines = []
temp_list = []
code_list = []
resultstr = ""
startSeq = []
endSeq = []


def appendingFunc(st, ed):
    for i in range(st, ed):
        print(i, end=' ')
        code_list.append(temp_list[i])

    print(*code_list)


def startMulti(k1, temp_list, ln):
    startSeq.append(k1)

    print(k1, ln)


def startMultiEnd(k2, temp_list, ln):
    endSeq.append(k2)
    print(k2, ln)


def removeMultiLine(temp_list, ln):

    # print(*temp_list, ln)
    k1 = 0
    k2 = 0

    for i in range(ln-1):
        if (temp_list[i] == "/" and temp_list[i+1] == "*"):
            k1 = i
            startMulti(k1, temp_list, ln)
        if (temp_list[i] == "*" and temp_list[i+1] == "/"):
            k2 = i
            startMultiEnd(k2, temp_list, ln)


if __name__ == "__main__":

    code_ws_comment = open(
        'C:/Users/G/Documents/python programs/sample sql_script.sql').read()
    # string

    lines = code_ws_comment.split("\n")  # lines
    for line in lines:
        l = len(line)
        count = 0
        for i in range(l):
            if (i == l):
                break
            else:
                for j in range(i + 1, l):
                    if (line[i] == "-" and line[j] == "-"):
                        count = line.index(line[i])
                # print(count)
                if (count > 0):
                    temp_list.append(line[i:count])
                else:
                    temp_list.append(line[i])
    # print(*temp_list)
    print("let's see for the multiple lines")
    ln = len(temp_list)
    # print(*temp_list)

    removeMultiLine(temp_list, ln)
    print(startSeq, endSeq)
    lenEndSeq = len(endSeq)
    g = 0
    t = 0
    while(lenEndSeq):

        appendingFunc(t, startSeq[g])
        t = endSeq[g]

        lenEndSeq = lenEndSeq - 1
        g = g+1

"""
lines = []
temp_list = []
code_list = []
resultstr = ""

code_ws_comment = open(
    'C:/Users/G/Documents/python programs/sample sql_script.sql').read()
# string

lines = code_ws_comment.split("\n")  # lines
for line in lines:
    l = len(line)
    count = 0
    for i in range(l):
        if (i == l):
            break
        else:
            for j in range(i + 1, l):
                if (line[i] == "-" and line[j] == "-"):
                    count = line.index(line[i])
            # print(count)
            if (count > 0):
                temp_list.append(line[i:count])
            else:
                temp_list.append(line[i])
# print(*temp_list)
print("let's see for the multiple lines")
ln = len(temp_list)


def removeEndComm(count2):
    return count2


def removeStartCom(count1):
    startIndex = count1
    endIndex = removeEndComm
    for k in range(startIndex):
        code_list.append(temp_list[k])

        x = k
        if k == startIndex:
            break
    temp = x
    print(*code_list)

    # code_list.append(temp_list[k])
    # print(*code_list)

    # print(*code_list)

    # for p in range(count2, ln):
    #     code_list.append(temp_list[p])
    #     print(temp_list[count2])


ln = len(temp_list)

for i in range(ln):
    if (i == ln):
        break
    rangecount = 0
    count1 = 0
    count2 = 0
    temp = 0

    for j in range(i + 1, ln):
        if (rangecount < 1):
            if (temp_list[i] == "/" and temp_list[j] == "*"):
                count1 = i
                # print(count1)
                removeStartCom(count1)

                # for k in range(count1):
                #     code_list.append(temp_list[k])
                # print(temp_list[count1])

            if (temp_list[i] == "*" and temp_list[j] == "/"):
                count2 = j + 1
                # print(count2)
                removeEndComm(count2)

                # for p in range(count2, ln):
                #     code_list.append(temp_list[p])
                # print(temp_list[count2])
        rangecount += 1
"""

# for r in code_list:
#     resultstr = resultstr+r
# print(resultstr)


# lines = []
# temp_list = []
# code_list = []
# resultstr = ""
# code_ws_comment = open(
#     'C:/Users/G/Documents/python programs/sample sql_script.sql').read()
# # string

# lines = code_ws_comment.split("\n")  # lines
# for line in lines:
#     l = len(line)
#     count = 0
#     for i in range(l):
#         if (i == l):
#             break
#         else:
#             for j in range(i + 1, l):
#                 if (line[i] == "-" and line[j] == "-"):
#                     count = line.index(line[i])
#             print(count)
#             if (count > 0):
#                 temp_list.append(line[i:count])
#             else:
#                 temp_list.append(line[i])
# print(*temp_list)
# print("let's see for the multiple lines")
# ln = len(temp_list)

# for i in range(ln):
#     rangecount = 0
#     count1 = 0
#     count2 = 0
#     if (i == ln):
#         break
#     else:
#         for j in range(i + 1, ln):
#             if (rangecount < 1):
#                 if (temp_list[i] == "/" and temp_list[j] == "*"):
#                     count1 = i
#                     print(count1)
#                     for k in range(count1):
#                         code_list.append(temp_list[k])
#                     # print(temp_list[count1])
#                 if (temp_list[i] == "*" and temp_list[j] == "/"):
#                     count2 = j + 1
#                     print(count2)
#                     for p in range(count2, ln):
#                         code_list.append(temp_list[p])
#                     # print(temp_list[count2])
#             rangecount += 1

# for r in code_list:
#     resultstr = resultstr+r
# print(resultstr)
