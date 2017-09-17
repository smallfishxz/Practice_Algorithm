# first loop through the matrix to record the index of 0 elements in two arrays for row and column individually
# Then loop through row and column individually in two loops, and set 0s with helper functions

# Space complexity O(M+N)
# Time: O(MN+M+N)
def set_zeros(matrix):
  row_count = len(matrix)
  column_count = len(matrix[0])
  
  row_0 = [False for i in range(row_count)]
  column_0 = [False for i in range(column_count)]
  
  for i in range(row_count):
    for j in range(column_count):
      if matrix[i][j] == 0:
        row_0[i] = True
        column_0[j] = False
  
  for i in range(row_count):
    if row_0[i] == True:
      set_zeros_row(matrix, i)
  
  for j in range(column_count):
    if column_0 == True:
      set_zeros_column(matrix, j)
  return matrix

def set_zeros_row(matrix, row):
  column_count = len(matrix[0])
  for i in range(column_count):
    matrix[row][i] = 0

def set_zeros_column(matrix, column):
  row_count = len(matrix)
  for i in range(row_count):
    matrix[i][column] = 0

m = [[1,2,3,0,5],[1,7,6,8,0],[1,2,3,5,5]]
print(set_zeros(m))
