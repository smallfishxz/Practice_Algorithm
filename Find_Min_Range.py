# NSortedArrays
# [edit]Find the shortest range that would have at least one entry from each of the input N sorted integer arrays 

# Interview: Onsite - Coding
# Author:Veera

# [edit]Question 

# A sample input could be  A1 = [10, 15, 21, 31, 33]  A2 = [7, 16, 20, 27]  A3=  [12, 22, 29, 34]  Sol: 20-22

# Explain what a range is e.g. range 4-8 => 4, 5, 6, 7, 8 on number line. Give an example that contains one element from each array (7-12) Hints: The data is sorted, How can range be reduced? 

# Brute force solution is to iterate over the give arrays finding minimum range. Good candidates usually optimize this right away.

# One possible solution is to pick first element of each array, calculate range, compare it global range, replace global range if current range is smaller and replace the min element in this list with the next element from the parent array. For the above

# tmp = [10, 7 ,12] range = 7-12 length=6, global range=7,12

# tmp = [10, 16, 12] range = 10-16 length=7, global range = 7,12 ...

# Good candidates should be able to convert the algorithm to code without much help.
# Sample solution:

def find_min_range_1(list_of_lists):
  if len(list_of_lists) == 0:
    return (None, None)
  min_range={}
  ind_list = [0 for i in range(len(list_of_lists))]
  
  while True:
    try:
      ele_list = [arr[i] for arr, i in zip(list_of_lists, ind_list)]
    except IndexError:
      break
    
    min_ele = min(ele_list)
    max_ele = max(ele_list)
    min_range[max_ele-min_ele]=(min_ele, max_ele)
    min_index = ele_list.index(min_ele)
    ind_list[min_index] += 1
   
  return (None, None) if len(min_range) == 0 else min_range[min(min_range.keys())]

print(find_min_range_1([[10,15,21,31,33],[7,16,27],[12,29,34]]))

# Offical answer
# def find_min_range( list_of_lists):
#   if (len(list_of_lists) < 1):
#     return None, None
#   min_range = {}
#   idx_list = [0] * len(list_of_lists)
#   while True:
#     try:
#       # Can use a better data structure
#       elem_list = [arr[i] for arr, i in zip(list_of_lists, idx_list)]
#     except IndexError:
#       break
#     # Alternatively
#     l_min = min(elem_list)
#     l_max = max(elem_list)
#     l_min_idx = elem_list.index(l_min)
#     min_range[l_max-l_min] = (l_min, l_max)
#     idx_list[l_min_idx] = idx_list[l_min_idx] + 1
#   return (None, None) if len(min_range) == 0 else min_range[min(min_range.keys())]
    
