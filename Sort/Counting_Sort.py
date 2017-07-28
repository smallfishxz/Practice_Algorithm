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

# Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
# Auxiliary Space: O(n+k)

# Points to be noted:
# 1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
# 2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data.
# 3. It is often used as a sub-routine to another sorting algorithm like radix sort.
# 4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
# 5. Counting sort can be extended to work for negative inputs also.
