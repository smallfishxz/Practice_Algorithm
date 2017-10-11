# Question reference: http://www.geeksforgeeks.org/pancake-sorting/

# find max_index in A[0:n-1]
def find_max(A, n):
  mi = 0
  for i in range(n):
    if A[i]>A[mi]:
      mi=i
  return mi

def find_max1(A,n):
  mi=0
  max=A[0]
  for i in range(1,n):
    if A[i]>max:
      mi=i
      max=A[i]
  return mi
  
# Reverses arr[0..i]
def flip(A,i):
  start=0
  while (start<i):
    A[i], A[start] = A[start], A[i]
    start+=1
    i-=1
  return A

def flip_sort(A):
  cur_size = len(A)
  
  while cur_size > 0:
    m_index=find_max(A,cur_size)
    if m_index != cur_size-1:
      print(m_index)
      # first flip max to beginning
      A=flip(A,m_index)
      print(A)
      # flig max to end
      A=flip(A,cur_size-1)
    cur_size-=1
  return A
  
# print(find_max1([5,3,7,9],3))
print(flip_sort([23, 10, 20, 11, 12, 6, 7]))
