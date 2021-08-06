filePath = r"C:\Users\G\Desktop\programs\python TCS\FileOperationsPrograms\sampleTextFile.txt"
file = open(filePath, "r")
noLines = 0
noWords = 0
noCharacters = 0

for line in file:
    line = line.strip("\n")
    noLines += 1
    words = line.split()
    noWords += len(words)

    noCharacters += len(line)

file.close()

print("No of Lines: ", noLines)
print("No of Words: ", noWords)
print("No of Characters: ", noCharacters)
