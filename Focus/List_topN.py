import heapq

# min-heap. 
# Time complexity: O(n+klogn): O(n) to build the heap, this is possible using bottom-up heap construction
# and to pop min element from heap for k times, while each pop takes O(logn)
# space: extra O(n) for the heap

def find_closest(arr, k):
  h = []
  size = len(arr)
  for i in range(size):
    d = arr[i][0]*arr[i][0] + arr[i][1]*arr[i][1]
    heapq.heappush(h, (d, arr[i]))
  
  print(h)
  
  i = 0
  closest = []
  while i < k and h:
    closest.append(h[0][1])
    heapq.heappop(h)
    i += 1
 
  return closest
  
# min heap on minus distance, which is effectively the max heap
# Time: O(klogk+(n-k)logk)) =  O(nlog k)
# space:  uses O(k) additional space
def find_closest2(arr, k):
  h = []
  size = len(arr)
  for i in range(k):
    d = - (arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1])
    heapq.heappush(h, (d, arr[i]))
  
  closest = []
  for i in range(k, size):
    d = - (arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1])
    if d > h[0][0]:
      heapq.heappushpop(h, (d, arr[i]))
  return h

# selection sort.
# time: O(nk)
def find_closest3(arr, k):
  size = len(arr)
  for i in range(k):
    min_inx = i
    min_d = arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1]
    for j in range(i+1, size):
      cur_d = arr[j][0]*arr[j][0]+arr[j][1]*arr[j][1]
      if cur_d < min_d:
        min_inx = j
    
    arr[i], arr[min_inx] = arr[min_inx], arr[i]
  
  return arr[0:k]
      
print(find_closest3([(2,2), (3,3), (1,1)], 2))
