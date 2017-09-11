# for sparse vector, it would be more efficient to build a dense vector on top of it, which is basically recording the non-zero element and its index in the origianal list
def build_dense_array(arr):
  d_arr = []
  for i in range(len(arr)):
    if arr[i] != 0:
      d_arr.append((i, arr[i]))
  return d_arr
  
# then generate the dot production for two densed list
# loop through both dense list with two pointers
# if index memeber of arr1 current pointer element < arr2's, increase the arr1 pointer
# if index memeber of arr1 current pointer element > arr2's, increase the arr2 pointer
# if they equal, meaning that the value member of both poiter element in arr1 and arr2 should be counted into the dot production
def dot_production(d_arr1, d_arr2):
  if len(d_arr1) == 0 or len(d_arr2) == 0:
    return 0
  
  i, j, result = 0, 0, 0
  while i < len(d_arr1) and j < len(d_arr2):
    index_i, index_j = d_arr1[i][0], d_arr2[j][0]
    if index_i < index_j:
      i += 1
    elif index_i > index_j:
      j += 1
    else:
      result += d_arr1[i][1] * d_arr2[j][1]
      i += 1
      j += 1

  return result

# optimize to avoid unnecessary test
def dot_production2(d_arr1, d_arr2):
  if len(d_arr1) == 0 or len(d_arr2) == 0:
    return 0
  
  i, j, result = 0, 0, 0
  # while i < len(d_arr1) and j < len(d_arr2):
  while True:
    index_i, index_j = d_arr1[i][0], d_arr2[j][0]
    if index_i < index_j:
      i += 1
      if i == len(d_arr1):
        print('going to break1')
        break
    elif index_i > index_j:
      j += 1
      if j == len(d_arr2):
        print('going to break2')
        break
    else:
      result += d_arr1[i][1] * d_arr2[j][1]
      i += 1
      j += 1
      if i == len(d_arr1) or j == len(d_arr2):
        print('going to break3')
        break
      
  return result
  
dense_A = build_dense_array([2, 4, 0, 0, 0, 6])
dense_B = build_dense_array([0, 3, 4, 0, 0, 7, 8])
print(dense_A)
print(dense_B)

print(dot_production2(dense_A, dense_B))

# Following discussion:
# if one array is much longer than the other one, it should be optimized to use binary search to search every element in shorter 
# array in the longer array
# Also the binary search could have a lower bound. As long as one match is found, the next lower bound could be the returnd index + 1
# Howerver, this could be helpful too much if no match could be found, as no lower bound could be figured out
# another opmization could be earlier break for the loop of shorter array, once it is found that the lower bound is already
# bigger than the length of longer array, like [(1,x), (2,x), (100,x), (101,x)], [(1,x), (2,x), (3,x), (4,x), (5,x), (100,x)]
