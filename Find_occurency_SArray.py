def find_first(A,n):
  l=0
  h=len(A)-1
  while l<=h:
    mid=(l+h)//2
    if A[mid]==n and A[mid-1]<n:
     return mid
    elif A[mid]==n and A[mid-1]==n:
      h=mid-1
    elif A[mid]<n:
      l=mid+1
    else:
      h=mid-1
  return -1


def find_last(A,n):
  l=0
  h=len(A)-1
  while l<=h:
    mid=(l+h)//2
    # print(mid)
    if A[mid]==n and A[mid+1]>n:
     return mid
    elif A[mid]==n and A[mid+1]==n:
      l=mid-1
    elif A[mid]>n:
      h=mid-1
      # print(A[l:h])
    else:
      l=mid-1
      # print(A[l:h])
  return -1

def occurency(A,n):
  i=find_first(A,n)
  if i == -1:
    return -1
  j=find_last(A,n)
  
  return j-i+1

print (occurency([1,2,3,7,7,7,7,9,9], 7))

print (find_first([1,2,3,7,7,7,7,9,9], 7))
print (find_last([1,2,3,7,7,7,7,9,9], 7))
