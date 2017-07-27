# Reference: http://www.geeksforgeeks.org/selection-sort/

def selection_sort(A):
  # Traverse through all array elements
  for i in range(len(A)):
    min_ind = i
    # Find the minimum element in remaining 
    # unsorted array
    for j in range(i+1, len(A)):
      if A[min_ind] > A[j]:
        min_ind = j
    # Swap the found minimum element with 
    # the first element 
    A[i], A[min_ind] = A[min_ind], A[i]
  return A

print(selection_sort([64,25,12,22,11]))

# Time Complexity: O(n2) as there are two nested loops.

# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
