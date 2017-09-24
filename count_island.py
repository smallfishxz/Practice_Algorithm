
# A function to check if a given cell 
# (row, col) can be included in DFS
def is_included(i, j, m, visited):
  r_count = len(m)
  c_count = len(m[0])
  # only include the cell when index falls into the range, non_visited, and cell value = 1
  return (i >= 0 and i < r_count and
          j >= 0 and j < c_count and
          not visited[i][j] and m[i][j]==1)

# A utility function to do DFS for a 2D 
# boolean matrix. It only considers
# the 4 neighbours as adjacent vertices
def DFS(matrix, i, j, visited):
  
  # index difference for the 4 cells surrounded the cell [i][j]. And these are the 4 concerning cells to do DFS
  row_n = [ -1, 0, 0, 1]
  col_n = [ 0, -1, 1, 0]
  
  # Mark this cell as visited
  visited[i][j] = True
  
  # Recur for all connected neighbours
  for k in range(4):
    if is_included(i+row_n[k], j+col_n[k], matrix, visited):
      DFS(matrix, i+row_n[k], j+col_n[k], visited)

# The main function that returns
# count of islands in a given boolean
# 2D matrix
def countIslands(matrix):
  row_count = len(matrix)
  col_count = len(matrix[0])
  # initialize a visited matrix to indicate whether a cell has been visited
  visited = [[False for j in range(col_count)] for i in range(row_count)]
  
  # Initialize count as 0 and travese 
  # through the all cells of
  # given matrix
  count = 0
  for i in range(row_count):
    for j in range(col_count):
      # If a cell with value 1 is not visited yet, 
      # then new island found
      if visited[i][j] == False and matrix[i][j] ==1:
        # Visit all cells in this island 
        # and increment island count
        DFS(matrix, i, j, visited)
        count += 1
  return count


# FB solution
def flood(matrix, i, j):
  matrix[i][j] = False
  def consider(i, j):
      if i in range(len(matrix)) and j in range(len(matrix[i])) and  matrix[i][j]:
          flood(matrix, i, j)
  consider(i + 1, j)
  consider(i, j + 1)
  consider(i - 1, j)
  consider(i, j - 1)

def count_islands(matrix):
  count = 0
  for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if matrix[i][j]:
              count += 1
              flood(matrix, i, j)
  return count
  

m = [1, 1, 0, 0, 0],[0, 1, 0, 0, 1],[1, 0, 0, 1, 1],[0, 0, 0, 0, 0],[1, 0, 1, 0, 1]
# print(count_islands(m))
print(countIslands(m))
