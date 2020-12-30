ROW,COL=map(int,input().split())
grid = []
pri=0
def isvalid(row, col, prevRow, prevCol):
   return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and not (row== prevRow and col == prevCol)
rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
colNum = [-1, 0, 1, -1, 1, -1, 0, 1]
def DFS(mat, row, col,prevRow, prevCol, word,path, index, n):
   if (index > n or mat[row][col] != word[index]):
        return
   path += word[index] + "(" + str(row)+ ", " + str(col) + ") "
   if (index == n):
       pri=1
       print('YES')
       quit()
   for k in range(8):
       if (isvalid(row + rowNum[k], col + colNum[k],prevRow, prevCol)):
           DFS(mat, row + rowNum[k], col + colNum[k],row, col, word, path, index + 1, n)


def findWords(mat,word, n):
   for i in range(ROW):
       for j in range(COL):
           if (mat[i][j] == word[0]):
               DFS(mat, i, j, -1, -1, word, "", 0, n)


for i in range(ROW):
    grid.append(list(map(str,input().split())))
s=input().strip()
findWords(grid, s, len(s) - 1)
print(pri)
if pri==0:print('NO')
        

