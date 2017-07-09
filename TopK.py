import heapq

def topK(A,k):
  h=[]
  for i in range(0,k-1):
    heapq.heappush(h,A[i]) 
  for i in range(k, len(A)-1):
    if A[i] > h[0]:
      heapq.heappushpop(h,A[i])
  return h
  
print(topK([10,7,6,5],3))

# Python heap implementation: 
# http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html#fig-percup
