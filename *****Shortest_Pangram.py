import sys

def find_sub(input, pattern):
  for outer in range(len(pattern), len(input)):
    for inner in range(0, len(input)-outer):
      window = input[inner:inner+outer]
      if set(window) >= set(pattern):
        return window
  return -1

def find_sub_1(input,pattern):
  l1=len(input)
  l2=len(pattern)
  
  if l1<l2:
    return -1
  
  hash_i={c:0 for c in set(pattern)}
  hash_p={c:0 for c in set(pattern)}
  
  for c in pattern:
    hash_p[c]+=1
  
  count = 0
  start = 0
  min_len = sys.maxsize
  start_index = -1
  
  for j in range(l1):
    if input[j] in hash_p:
      hash_i[input[j]]+=1
      count+=1
    if count==len(hash_p):
      while start<j and hash_i[input[start]] > hash_p[input[start]]:
        hash_i[input[start]]-=1
        start+=1
      window_len = j-start+1
      if min_len > window_len:
        min_len = window_len
        start_index = start
  
  if start_index == -1:
    return -1
  return input[start_index:start_index+min_len]
  
# print(find_sub('aaccbcd','abc'))

print(find_sub_1('aaccbcd','abc'))
      
