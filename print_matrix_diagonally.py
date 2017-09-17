# Given a matrix of mxn dimensions, print the elements of the matrix in diagonal order.

# Algorithm:
# rowCount = number of rows
# columnCount = number of columns
# Then, number of diagonals will be = rowCount + columnCount - 1

# Step 1: Print first rowCount diagonals 
# Print diagonals that start from the first column 
# elements.

# Step 2: Print next columnCount - 1 diagonals 
# Print diagonals that start from the last row 
# elements.

# Step 1 Details: Print first rowCount diagonals 
# Iterate to print diagonals from row k = 0 to rowCount - 1.
# 1: Start with row = k and col = 0
# 2: Print the element matrix[row][col]
# 3: Decrement row by 1 Increment col by 1till row greater than or equal to 0 and  col less than columnCount

# Step 2 Details: Print next columnCount – 1 diagonals 
# Iterate to print diagonals from column k = 1 to columnCount - 1
# 1: Start with last row, row = rowCount – 1 and col = k
# 2: Print the element matrix[row][col]
# 3: Decrement row by 1 Increment col by 1till row greater than or equal to 0 and  col less than columnCount

# Order of the Algorithm:
# Time Complexity: O(mn)
# Space Complexity: O(1)

def print_matrix_diagonally(matrix):
  row_count = len(matrix)
  column_count = len(matrix[0])
  
  for i in range(row_count):
    row, column = i, 0
    while row >= 0 and column < column_count:
      print(matrix[row][column])
      row -= 1
      column += 1
  
  for i in range(1, column_count):
    row, column = row_count-1, i
    while row >= 0 and column < column_count:
      print(matrix[row][column])
      row -= 1
      column += 1

def print_matrix_diagonally2(matrix):
  row_count = len(matrix)
  column_count = len(matrix[0])
  
  for i in range(column_count):
    row, column = 0, i
    while row < row_count and column >= 0:
      print(matrix[row][column])
      row += 1
      column -= 1
  
  for i in range(1, row_count):
    row, column = i, column_count-1
    while row < row_count and column >= 0:
      print(matrix[row][column])
      row += 1
      column -= 1


print_matrix_diagonally2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
