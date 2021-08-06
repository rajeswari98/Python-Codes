#working with dictionaries
#swapping the dictionaries values with keys and values.

db = {1: 'a', 2: 'b', 3: 'c', 4: 'c'}#input

# o_db = {​​​​​​​​'a':1, 'b':2, 'c':[3,4]}​​​​​​​​#output
k = {}
for key, value in db.items():
    if value in k:
        k[value].append(key)
    else:
        k[value] = [key]
print(k)
