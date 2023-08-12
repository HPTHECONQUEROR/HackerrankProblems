matrix=[ [1,2,3],
         [4,5,6],
         [7,8,9]]
print(matrix[2][2])#THIS CAN SHOW THE ELEMENT IN [2][2] ie..,9
matrix[2][2]=10
print(matrix[2][2],"\n")#THIS CAN CHANGE THE VALUE OF [2][2] VALUE INTO 10


for row in matrix:
    print(row)
    for e in row:
     print(e)