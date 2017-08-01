# Reference: http://www.geeksforgeeks.org/insertion-sort/

def insertion_sort(A):
  # Traverse through 1 to len(arr)
  for i in range(1, len(A)):
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    key = A[i]
    j = i-1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key
  return A

# Time Complexity: O(n*n)
# Auxiliary Space: O(1)
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
# Algorithmic Paradigm: Incremental Approach
# Sorting In Place: Yes
# Stable: Yes
# Online: Yes
# Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.


# Reference: https://jeffreystedfast.blogspot.com/2007/02/binary-insertion-sort.html
def binary_search(arr, l, h, element):
  # return l when l equals to h as element doesn't necessarily exist, and we only need to find the perfect insertion poo
  if l == h:
    return l;
  m = l+(h-l)//2
  if element < arr[m]:
    return binary_search(arr, l, m, element)
  elif element > arr[m]:
    return binary_search(arr, m+1, h, element)
  return m

def insertion_sort_bsearch(A):
  for i in range(1, len(A)):
    key = A[i]
    j = i-1
    print(key, j)
    pos = binary_search(A, 0, j, key)
    print(pos)
    while j >= pos:
      A[j+1] = A[j]
      j -= 1
    A[pos] = key
  return A

# print(binary_search([11,12,22,25,64], 0, 4, 25))    
print(insertion_sort_bsearch([64,25,12,22,11]))
# Time Complexity: The algorithm as a whole still has a running worst case running time of O(n2) because of the series of swaps required for each insertion.
