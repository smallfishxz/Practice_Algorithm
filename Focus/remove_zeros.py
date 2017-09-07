# Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements.

# Difficulty:  Easy

# Loop from both ends till they meet
# For elements on left, if it is non-zero, leave it there, else have the non-zero on right to overwrite this zero
# for elements on right, if it is zero, leave it there. if it is non-zero, look for having it overwriting the zero on left

def remove_zeros(arr):
  l = 0
  r = len(arr) - 1
  while l <= r:
    if arr[l] != 0:
      l += 1
    elif arr[r] == 0:
      r -= 1
    else:
      arr[l] = arr[r]
      l += 1
      r -= 1
  return arr
  
print(remove_zeros([0,1,2,0,3,0,3]))
