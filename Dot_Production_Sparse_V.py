def build_dense_array(A):
  d_A = []
  for i in range(len(A)):
    if A[i] != 0:
      d_A.append((i, A[i]))
  return d_A

def dot_prod(dA, dB):
  if len(dA) == 0 or len(dB) == 0:
    return 0
  i, j, result = 0, 0, 0
  while (i < len(dA) and j < len(dB)):
    index_i, index_j = dA[i][0], dB[j][0]
    if index_i < index_j:
      i += 1
    elif index_i > index_j:
      j += 1
    else:
      result += dA[i][1]*dB[j][1]
      i += 1
      j += 1
  return result

dense_A = build_dense_array([2, 4, 0, 0, 0, 6])
dense_B = build_dense_array([0, 3, 4, 0, 0, 7, 8])

print(dot_prod(dense_A, dense_B))

# 1. Discuss worst-case complexity. What is the complexity? Correct answer: O(n1 + n2) or O(max(n1, n2)). 
# If candidate says otherwise, work together to reach the right solution with e.g. examples.
# 2. Let's say we use the code in production for a while and we figure that very often one of the two vectors is much shorter 
# than the other. What can we do to improve complexity for these situations? 
# The expected answer: an algorithm that iterates linearly the shorter vector and does binary search in the longer one. 
# Complexity is O(min(n1, n2) log(max(n1, n2))). 
# Usually candidates don't have the time to actually implement the binary search part, 
# but they should be able to describe the idea and assess complexity.
# 3. Binary search with optimization: do you really need to do a binary search over the entire larger array every time 
# you iterate through the shorter array?
# Good candidates should figure that after each binary search they can eliminate the entire portion to the left 
# at the found position. This is because the shorter vector is also sorted so there's no chance lower indexes will ever match. 
# Question for candidate: does this improve the worst case complexity? Correct answer: it shouldn't, because if e.g. the largest index in the shorter array is smaller than the smallest index in the larger array, binary search will return virtually no information. Good candidates should be able to produce this or a similar example to justify their response.
# Advanced: binary search has terrible cache behavior - jumps all over the place. 
# How can we make the algorithm cache friendlier without sacrificing log behavior? 
# Answer: start from the left edge and use an exponentially-increasing gait (1, 2, 4, 8, ...). 
# This keeps complexity the same but is more cache friendly. Most candidates don't answer this, 
# but it's worth discussing it a bit with the advanced ones.


    
