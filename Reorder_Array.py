
# Given a function that takes as input two arrays of the same length, A and O, reorder A according to the elements in O. 
# The A array is an array of opaque objects. 
# The O array contains the ordering information such that each element in O indicates the position the corresponding element in A belongs in. 
# On input, the two arrays are given. On completion, the caller expects A to be re-ordered and does not care about O 
# (i.e. the function can do whatever it wants to O). I give the following function prototype and sample data:

#  	 0 	 1 	 2 	 3 	 4
# A 	 E 	 A 	 B 	 D 	 C
# O 	 4 	 0 	 1 	 3 	 2
# I use letters in the sample data to demonstrate that if the A array were reordered according to the O array, it would be alphabetically ordered:

#  	 0 	 1 	 2 	 3 	 4
# A 	 A 	 B 	 C 	 D 	 E
# I make it clear that the elements in A are not actually letters -- they are opaque objects.

def reorder_1(A,B):
  i=0
  while i<len(A):
    if B[i]==i:
      i+=1
      continue
    
    target_index=B[i]
    # swap A
    tmp_a=A[i]
    A[i]=A[target_index]
    A[target_index]=tmp_a
    
    # swap B accordingly
    tmp_b=B[i]
    B[i]=B[target_index]
    B[target_index]=tmp_b
  return A

def reorder_2(A,B):
  C=[0 for tmp in range(len(A))]
  for i in range(len(A)):
    C[B[i]]=A[i]
  A=C
  return A

print(reorder_2(['E','A','B','D','C'],[4,0,1,3,2]))
