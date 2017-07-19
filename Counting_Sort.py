# http://www.geeksforgeeks.org/counting-sort/

def counting_sort(A, M):
  count = [0 for i in range(M)]
  output = [0 for i in range(len(A))]
  
  for i in range(len(A)):
    count[A[i]] += 1
  print(count)
  for i in range(1, M):
    count[i] = count[i-1]+count[i]
  print(count)
  
  for i in range(len(A)):
    output[count[A[i]]-1] = A[i]
    count[A[i]] -= 1
  print(output)
  
  for i in range(len(A)):
    A[i] = output[i]
  
  return A

print(counting_sort([1,4,1,2,7,5,2], 10))
