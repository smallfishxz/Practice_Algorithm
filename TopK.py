import heapq

# O: (n-k)logk, space: K
def topK(A,k):
  h=[]
  # Use Python native heap to build a min heap for the first k elements of the array
  for i in range(0,k-1):
    heapq.heappush(h,A[i]) 
  # Loop through the element after kth element. If it is bigger than the min in heap, pop heap and push that element into heap  
  for i in range(k, len(A)-1):
    if A[i] > h[0]:
      heapq.heappushpop(h,A[i])
  return h

# O: nk, space: 0
def topk_bubble_sort(A,k):
  ll = len(A)
  # Modify the outer loop of bubble sort for k times instead of len(A)
  for i in range(k):
    swap_flag = False
    for j in range(0, ll-i-1):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]
        swap_flag = True
    if swap_flag == False:
      break
  return A[ll-k:]

# print(topk_bubble_sort([10,7,6,5],4))

print(topK([10,7,6,5],3))

# Python heap implementation: 
# http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html#fig-percup
