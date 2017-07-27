def bucket_sort(A):
  m = max(A)
  buckets = [[] for i in range(len(A))]
  for i in range(len(A)):
    index = (A[i]*len(A))/(m+1)
    buckets[index].append(A[i])
  out = []
  for buck in buckets:
    out += i_sort(buck)
  return out

def i_sort(B):
  for i in range(1, len(B)):
    key = B[i]
    j = i-1
    while j >=0 and key < B[j]:
      B[j+1]=B[j]
      j=j-1
    B[j+1]=key
  return B
    
print(i_sort([11,12,8,9,1]))

# bucket sort reference: http://www.geeksforgeeks.org/bucket-sort-2/
# Another bucket sort sample code: https://gist.github.com/sahid/5022081
