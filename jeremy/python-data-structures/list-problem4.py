matrix = [[2,5,3],[7,0,8],[9,4,1]]
matrix_row_sums = []

for row in matrix:
    matrix_row_sums.append(sum(row))

print(matrix[0],matrix[1],matrix[2])
print(matrix_row_sums)
print(matrix[0][0],matrix[1][1],matrix[2][2])