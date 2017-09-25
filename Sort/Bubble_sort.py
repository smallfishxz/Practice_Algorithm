# references: http://www.geeksforgeeks.org/bubble-sort/

def bubble_sort(arr):
  size = len(arr)
  # Transverse each element
  for i in range(size):
    swap_flag = False
    # as for inner loop, the last i element aleady in place
    for j in range(0, size-i-1):
      # swap if current element is bigger than its next element
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap_flag = True
    # if no swap happens for loop j, A is already sorted, break outer loop
    if swap_flag == False:
      break 
  return arr

print(bubble_sort([9,6,7,5,10]))
