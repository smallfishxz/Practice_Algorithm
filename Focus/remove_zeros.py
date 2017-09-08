# Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements.

# Difficulty:  Easy

# Loop from both ends till they meet
# For elements on left, if it is non-zero, leave it there, else have the non-zero on right to overwrite this zero
# for elements on right, if it is zero, leave it there. if it is non-zero, look for having it overwriting the zero on left

# Loop through the array with two pointers, both starts from the beginning
# fast one just increase by 1 every time, while slow one keeps track of the non-zero elements 
# Whenever fast points to a non-zero element, assign this one to the element pointed by the slow elements, only when slow doens't equal to fast (this is to avoid unnecessary assignment)

# Time cmoplexity is O(N), and the sequence of non-zero elements are preserved, so it is a stable algorithm.
# suppose array has k zero elements, then n-k writes are needed in worst case, and it happens when zeros are in the beginning
# of the array

# boundary check: no zeros, or all zeros
def remove_zeros_statble(A):
  slow = 0
  size = len(A)
  for fast in range(size):
    if A[fast] != 0:
      if slow != fast:
        A[slow] = A[fast]
      slow += 1
  return slow

# loop through the array with two pointers from both end together, till they meet
# if the left pointer points to non zero, leave it as it is,
# or, if the right pointer points to zero, leave it as it is too.
# then, if the left pointer points to zero while right pointer points to non-zero, assign right element to left element
# no need to swap as we dont care what are left on the right part of the array

# k is number of non-zero elements
# time complexity is O(n), and worst case the assignment needs to happen min(k, n-k) when zeros are in the beginning.
# k is the number of zero elements.
# 00123, assignment twice
# 0000123, assignment three times

def remove_zeros(A):
  i = 0
  j = len(A) - 1
  while i <= j:
    if A[i] != 0:
      i += 1
    elif A[j] == 0: 
      j -= 1
    else:
      A[i] = A[j]
      i += 1
      j -= 1
  
  return i

print(remove_zeros([0,1,2,0,3]))
