from collections import defaultdict

words = ['cat', 'lump', 'eat', 'me', 'tea', 'em', 'plum', 'god', 'dog']

temp = defaultdict(set)
for word in words:
    temp[str(sorted(word))].add(word)
res= list(temp.values())
print(res)
