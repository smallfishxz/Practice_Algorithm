# While looping through the array, at one integer, what you can get is the value of this element and the sum of elements before it and including it. 
# And if the sum before it and including it is negative, this tmp sum wont help to generate the biggest sum, so this tmp sum could be result to be 0, for next integer to start the new tmp sum from 0

import sys

def max_sum(s):
  running_s = 0
  max_s = -sys.maxsize
  size = len(s)
  
  for i in range(size):
    running_s += s[i]
    if running_s > max_s:
      max_s = running_s
    if running_s < 0:
      running_s = 0
  
  return max_s

print(max_sum([5,-3,-6,4,-5,10]))
