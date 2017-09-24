# Find the kth largest, equals to find the (n-k)th smallest
# Use min heap for top K largest, and use max heap for top n-k smallest

import heapq

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
  print(h)
  for i in range(heap_size, size):
    # when arr element is smaller than the minus (top element in the minheap) - top element is the smallest in the
    # minheap, so minus it means the biggest in the heap 
    if arr[i] < -h[0]:
      heapq.heappushpop(h, -arr[i])
    print(h)
  
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
    
print(kth_element_minheap([5,4,3,6,8], 4))  
print(kth_element_maxheap([5,4,3,6,8], 4))
print(kth_element_heap([5,4,3,6,8], 4))
