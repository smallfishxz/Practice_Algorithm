# Write a function that takes two parameters: (1) an integer N; and, (2) an array of integers.  
# The function should return a single, uniformly random integer between [0, N-1] such that the resulting integer is NOT 
# one of the integers you are given in the array.

# generate an allowed list first
# use the python random function to generate random integer for the index of allowed list
# return the item in allowed list with that random index

import random 

def rand_restr(N, forbidden):
  # build a set from the input array to remove dup and also make the lookup O(1) afterwards
  # O(len(forbidden)) to build this set
  forb_set = set(forbidden)
  
  #O(N) to build the allowed list
  allowed=[]
  for i in range(N):
    if i not in forb_set:
      allowed.append(i)
  
  # Corner case to consider for empty allowed list
  if not allowed:
    raise Exception ("All allowed elements [0, {s}) are forbidden!".format(s=N))
  
  r_ind = random.randint(0,len(allowed)-1)
  return allowed[r_ind]

print(rand_restr(5, [0,1,2,3,4]))
