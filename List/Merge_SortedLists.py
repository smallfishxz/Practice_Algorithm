# Loop through the two list at the same time, comparing current elements from both, add the smaller and non-dup one to final list
# how to decide it is non-dup: comparing the to-be added smaller element with the last element in final list.
def merge_list(l1, l2):
  i = 0
  j = 0
  result = []
  while i < len(l1) and j < len(l2):
    print('l1[{}] is: {}, l2[{}] is : {}'.format(i, l1[i], j, l2[j]))
    print(l1[i] <= l2[j])
    if l1[i] <= l2[j]:
      # if result is empty, directly append.
      if len(result) == 0 or result[-1] != l1[i]:
        result.append(l1[i])
        print(i, result)
      i += 1
    else:
      if len(result) == 0 or result[-1] != l2[j]:
        result.append(l2[j])
        print(j, result)
      j += 1
  
  while i < len(l1):
    if len(result) == 0 or result[-1] != l1[i]:
      result.append(l1[i])
    i += 1
  
  while j < len(l2):
    if len(result) == 0 or result[-1] != l2[j]:
      result.append(l2[j])
    j += 1
  
  return result

def merge_list1(l1, l2):
  return sort(set(l1+l2))
result = merge_list([1,1,2,4], [2,3,5])
print(result)
