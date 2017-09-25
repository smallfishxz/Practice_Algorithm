# Find the kth largest, equals to find the (n-k)th smallest
# Use min heap for top K largest, and use max heap for top n-k smallest

import heapq
import sys

def kth_element_minheap(arr, k):
  size = len(arr)
  h = []
  for i in range(k):
    heapq.heappush(h, arr[i])
  for i in range(k, size):
    if arr[i] > h[0]:
      heapq.heappushpop(h, arr[i])
  
  return h[0]

# build the 'maxheap' with Phtyon minheap to push the minus values of array into it.  
def kth_element_maxheap(arr, k):
  size = len(arr)
  h = []
  heap_size = size-k+1
  for i in range(heap_size):
    heapq.heappush(h, -arr[i])
  # print(h)
  for i in range(heap_size, size):
    # when arr element is smaller than the minus (top element in the minheap) - top element is the smallest in the
    # minheap, so minus it means the biggest in the heap 
    if arr[i] < -h[0]:
      heapq.heappushpop(h, -arr[i])
    # print(h)
  
  return -h[0]

# optimize to see whehther k is bigger/smaller than array size //2
# When k is long, meaning use the max heap is better, otherwise, use min heap
def kth_element_heap(arr, k):
  size = len(arr)
  h_max = []
  h_min = []
  if k >= size//2:
    for i in range(size-k+1):
      heapq.heappush(h_max, -arr[i])
    for i in range(size-k+1, size):
      if arr[i] < -h_max[0]:
        heapq.heappushpop(h_max, -arr[i])
    return -h_max[0]
  else:
    for i in range(k):
      heapq.heappush(h_min, arr[i])
    for i in range(k, size):
      if arr[i] > h_min[0]:
        heapq.heappushpop(h_min, arr[i])
    return h_min[0]

# In QuickSort, we pick a pivot element, then move the pivot element to its correct position and partition the array around it.
# The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. 
# Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. 
# The worst case time complexity of this method is O(n2), but it works in O(n) on average.
  
# Partition function is the same one as used in the quicksort algorithm
# it returns the index of the pivot element, and before this index, all elements are smaller than pivot element
# after this index, all elements are bigger than this element
# Also this function always pick the element at the high position
def partition(arr, low, high):
  i = low-1
  pivot = arr[high]
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  
  return i+1

# Use this function to get the kth smallest element in the array 
def kth_smallest_element_partition(arr, low, high, k):
  size = high-low+1
  # k needs to be bigger than 0 and within the array size
  if (k > 0 and k <= size):
    # first get the index of the pivot element 
    pi = partition(arr, low, high)
    # if the pivot element index is just the kth element we want to find, return
    if pi-low == k-1:
      return arr[pi]
    # if the pivot element index is bigger than the kth element index to find, like pivot is the 4th smallest, while trying to find the 3rd smallest, then the final result should be within the left part before the pivot index
    if pi-low > k-1:
      return kth_smallest_element_partition(arr, low, pi-1, k)
    # if the pivot element index is smaller than the kth element index to find, then final result should be within
    # the right part after the pivot index
    # NOTE: the k should be updated to count in the elements before the pivot index
    return kth_smallest_element_partition(arr, pi+1, high, k-(pi-low)-1)
  
  return sys.maxsize

# similarly with above, but transform the kth biggest element to n-k+1 smallest element within the function  
def kth_element_partition(arr, low, high, k):
  size = high-low+1
  new_k = size-k+1
  if (new_k > 0 and new_k <= size):
    pi = partition(arr, low, high)

    if pi-low == new_k-1:
      return arr[pi]
    if pi-low > new_k-1:
      return kth_smallest_element_partition(arr, low, pi-1, new_k)
  
    return kth_smallest_element_partition(arr, pi+1, high, new_k-(pi-low)-1)
  
  return sys.maxsize
  
# print(kth_element_minheap([5,4,3,6,8], 4))  
# print(kth_element_maxheap([5,4,3,6,8], 4))
print(kth_element_heap([5,4,3,6,8], 4))

print(kth_smallest_element_partition([5,4,3,6,8], 0, 4, 2))
print(kth_element_partition([5,4,3,6,8], 0, 4, 4))
