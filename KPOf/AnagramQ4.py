#Method 1 Time Complexity is O(N)
def printAnagramTogether(words):
    groupedWords = dict()
    temp=[]

    for word in words:
        word1 = ''.join(sorted(word))
        if word1 in groupedWords.keys():
            groupedWords[word1] += [word]
        else:
            groupedWords[word1] = [word]
    # print(groupedWords)
    for key,value in groupedWords.items():
        temp.append(set(value))
    return temp
# words = ['cat', 'lump', 'eat', 'me', 'tea', 'em', 'plum', 'god', 'dog']
words =['cat', 'dog', 'tac', 'god', 'act']
print(printAnagramTogether(words))



#Method 2 Time Complexity O(N)
# from collections import defaultdict

# words = ['cat', 'lump', 'eat', 'me', 'tea', 'em', 'plum', 'god', 'dog']

# temp = defaultdict(set)
# for word in words:
#     temp[str(sorted(word))].add(word)
# res= list(temp.values())
# print(res)
