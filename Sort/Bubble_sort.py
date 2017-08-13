# references: http://www.geeksforgeeks.org/bubble-sort/

def bubble_sort(A):
  for i in range(0,len(A)-1):
    swap_flag = False
    for j in range(0, len(A)-i-1):
      if A[j]>A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]
        swap_flag = True
      # print('(Outer loop {l1}, inner lopp {l2})'.format(l1=i, l2=j))
      # print(A)
    # if no swap happens for loop j, A is already sorted, break outer loop
    if swap_flag == False:
      break
  return A

print(bubble_sort([10,9,7,6,5]))
