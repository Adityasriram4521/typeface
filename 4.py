Given a matrix of 0's and 1's of size 256x256, write a program to print minimum sized sub-rectangle which includes all 0's of the matrix. Function needs to return the 4 corners of the minimum sized sub-rectangle.

Input:
1 0 0 1 1
1 0 0 0 1
1 0 0 1 1
1 1 1 1 1
Output
(0,1), (0, 3), (2, 1), (2, 3)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
matrix= []
for i in range(256):
    matrix.append(list(map(int, input().split())))

row1, row2, col1, col2 = 0, 0, 0, 0
for i in range(256):
    flag = True
    for j in range(256):
        if matrix[i][j] == 0:
            row1 = i
            flag = False
            break
    if not flag:
        break
    flag = True

for i in range(256):
    flag = True
    for j in range(256):
        if matrix[j][i] == 0:
            col1 = i
            flag = False
            break
    if not flag:
        break

for i in range(255, row1, -1):
    flag = True
    for j in range(256):
        if matrix[i][j] == 0:
            row2 = i
            flag = False
            break
