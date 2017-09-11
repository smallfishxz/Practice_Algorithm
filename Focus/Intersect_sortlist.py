# comparing with linear scan and binary search: 
# binary search works better than linear scan when ratio of larger length to smaller is more than logarithmic order.
# linear scan (LS) for length(a1) ~ length(a2) cases whereas binary search (BS) for length(a1) << length(a2) cases

# linear scan with two pointers
# if arr1 element < arr2 element, increase arr1 pointer
# if arr2 element > arr2 element, increase arr2 pointer
# if arr1 element = arr2 element, append it to result after confirm that it is not dup, increase both pointer
# time: O(m+n)

def intersect_arr(arr1, arr2):
  i, j = 0, 0
  size1 = len(arr1)
  size2 = len(arr2)
  result = []
  while i < size1 and j < size2:
    if arr1[i] < arr2[j]:
      i += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      if not result or result[-1] != arr1[i]:
        result.append(arr1[i])
      i += 1
      j += 1
  
  return result

# binary search
# search each element in the shorter array in the longer array
# have the lower boundary for the search to have better performance with shrinked search range. this is only benificial 
# when binary search could find a match index in the longer array. So it wont help much if there is not match in longer array 
# time: O(min(m,n)log(max(m,n))))
def b_search(A, l_bound, ele):
  low = l_bound
  high = len(A)
  
  while low <= high:
    mid = low + (high-low)//2
    if A[mid] == ele:
      return mid
    elif A[mid] < ele:
      low = mid + 1
    else:
      high = mid - 1
  return None
  
def intersect_arr2(arr1, arr2):
  result = []
  i, j = 0, 0
  # arr1 is designated as the shorter array
  if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1
 
  start = 0
  for i in range(len(arr1)):
    idx = b_search(arr2, start, arr1[i])
    print('search {} in arr2 from {}, and find it at {}'.format(arr1[i], start, idx))
    if idx:
      if not result or result[-1] != arr1[i]:
        result.append(arr1[i])
      start = idx + 1
      # have this break, to improve perfomance for situation like [1,100,101,200], [1,2,3,4,5,100], so that break after search for 100 in arr1
      if start >= len(arr2):
        break
  return result
 

    
print(intersect_arr2([1,3,3,4,7,11,107], [2,3,3,11,19]))
