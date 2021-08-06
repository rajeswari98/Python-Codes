infile = r"C:\Users\G\Desktop\programs\python TCS\FileOperationsPrograms\sampleTextFile.txt"
outfile = r"C:\Users\G\Desktop\programs\python TCS\FileOperationsPrograms\sampleTextopFile.txt"


def insert_line_para_nums(infile, outfile):
    f = open(infile, 'r')
    out = open(outfile, 'w')
    linecount = 0
    paragraphcount = 0
    empty = True
    for i in f:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
            if empty is True:
                paragraphnumber = 0
            else:
                paragraphnumber = paragraphcount
        out.write('%-4d %4d %s' % (paragraphnumber, linecount, i))
    f.close()
    out.close()
    print(paragraphnumber, linecount)


insert_line_para_nums(infile, outfile)
