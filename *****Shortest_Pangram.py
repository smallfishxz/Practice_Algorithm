# Reference: http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

import sys

def find_sub(input, pattern):
  for outer in range(len(pattern), len(input)):
    for inner in range(0, len(input)-outer):
      window = input[inner:inner+outer]
      if set(window) >= set(pattern):
        return window
  return -1

def find_sub(input, pattern):
  
  if len(input) < len(pattern):
    return -1
  
  # build the dictionary for patter string
  hash_p = {}
  for p in pattern:
    if p not in hash_p:
      hash_p[p] = 1
    else:
      hash_p[p] += 1
  
  hash_i={}
  size = len(input)
  count = 0
  start = 0
  min_window = sys.maxsize
  start_index = -1
  # Iterate through input string
  for i in range(size):
    print('loop {}:'.format(i))
    # build the dictionary for input string during each loop
    if input[i] not in hash_i:
      hash_i[input[i]] = 1
    else:
      hash_i[input[i]] += 1
    
    print(hash_i)
    
    # Count records how many characters in input string has matched with pattern. Increase the mactching count whenever a matching is found - char exists in pattern dictionary, and also the occurences in input dictionary is <= than the occurences in pattern dictionary
    if input[i] in hash_p and hash_p[input[i]] >= hash_i[input[i]]:
      count += 1
    
    # whenever a macthing is found, that is count == patten string length, start to shrink the window as much as possible
    if count == len(pattern):
      # loop through each charcter starting from the beginning of the string, and find the smallest window by shrinking under two conditions:
      # 1. char is not in pattern dictionary
      # 2. or, the occurences in input dictionary is bigger than occurences in pattern
      while input[start] not in hash_p or hash_i[input[start]] > hash_p[input[start]]:
        # under situation 2, update the input dictionary
        if input[start] not in hash_p:
          # increse the start char position if can shrink
          start += 1
        elif hash_i[input[start]] > hash_p[input[start]]:
          hash_i[input[start]] -= 1
          # increse the start char position if can shrink
          start += 1
        print('current hash_i is {}'.format(hash_i))
    
      # update window and the start index
      window_len = i - start + 1
      if window_len < min_window:
        min_window = window_len
        start_index = start
      print('min_window, start_index: {}, {}'.format(min_window, start_index))
      
  # if start_index = -1, no matching found
  if start_index == -1:
    return -1
  
  return input[start_index: start_index+min_window]
  
# print(find_sub('adccbcd', 'abc'))
print(find_sub('this is a test string','tist'))  
  
# print(find_sub('aaccbcd','abc'))

print(find_sub_1('this is a test string','tist'))
