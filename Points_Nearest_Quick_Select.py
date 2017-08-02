# This is based on the quick sort algorithm
# reference: https://rosettacode.org/wiki/Quickselect_algorithm#Python
# reference: https://en.wikipedia.org/wiki/Quickselect

import random

# find the kth smallest element in array
def partition(A, low, high, pivot_idx):
  # function to put all smallers before pivot_idx, and biggers after pivot_idx
  # i indicates the index of smaller numbers
  i = low
  pivot = A[pivot_idx]
  A[high], A[pivot_idx] = A[pivot_idx], A[high] # Move pivot to the end
  for j in range(low, high):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[high] = A[high], A[i]
  return i


# In quicksort, we recursively sort both branches, leading to best-case O(n log n) time. However, when doing selection, we already know which partition our desired element lies in, since the pivot is in its final sorted position, with all those preceding it in an unsorted order and all those following it in an unsorted order.

def quick_select_recursive(arr, low, high, k):
  # if arr has only 1 element, return this element
  if low == high:
    return arr[low]
  pivot_idx = random.randint(low, high)     # select pivotIndex between left and right
  pivot_idx = partition(arr, low, high, pivot_idx) # pivot is in its final sorted position
  if k == pivot_idx:
    return arr[k]
  elif k < pivot_idx:
    return quick_select_recursive(arr, low, pivot_idx-1, k)
  else:
    return quick_select_recursive(arr, pivot_idx+1, high, k)

def quick_select_loop(arr, low, high, k):
  while True:
    if low == high:
      return arr[low]
    pivot_idx = random.randint(low, high)     # select pivotIndex between left and right
    pivot_idx = partition(arr, low, high, pivot_idx)
    if k == pivot_idx:
      return arr[k]
    elif k < pivot_idx:
      high = pivot_idx-1
    else:
      low = pivot_idx+1

# without random pivot index
def partition_1(A, low, high):
  # function to put all smallers before pivot_idx, and biggers after pivot_idx
  # i indicates the index of smaller numbers
  i = low
  pivot = A[high]
  for j in range(low, high):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[high] = A[high], A[i]
  return i

# without random pivot index
def quick_select_recursive1(arr, low, high, k):
  # if arr has only 1 element, return this element
  if low == high:
    return arr[low]
  pivot_idx = partition_1(arr, low, high) # pivot is in its final sorted position
  if k == pivot_idx:
    return arr[k]
  elif k < pivot_idx:
    return quick_select_recursive1(arr, low, pivot_idx-1, k)
  else:
    return quick_select_recursive(arr, pivot_idx+1, high, k)

# without random pivot index
def quick_select_loop1(arr, low, high, k):
  while True:
    if low == high:
      return arr[low]
    pivot_idx = partition_1(arr, low, high)
    if k == pivot_idx:
      return arr[k]
    elif k < pivot_idx:
      high = pivot_idx-1
    else:
      low = pivot_idx+1
      
v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
print([quick_select_loop1(v, 0, 9, i) for i in range(10)])


    
  
