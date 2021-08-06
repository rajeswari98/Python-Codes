infile = r"C:\Users\G\Desktop\programs\python TCS\FileOperationsPrograms\sampleTextFile.txt"


def insertFileFunction(infile):
    file = open(infile, "r")
    linecount = 0
    paragraphCount = 0
    empty = True
    for i in file:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphCount += 1
                empty = False
            if empty is True:
                paragraphNumber = 0
            else:
                paragraphNumber = paragraphCount

    file.close()
    print("The total number of paragraphs are: ", paragraphNumber)


insertFileFunction(infile)
