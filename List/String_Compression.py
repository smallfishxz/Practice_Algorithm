# Iterate through the string char by char, and count its repeats. When next char is not the same as the current one, append the char and its repeats to the result string.
# In the end return the result string only when it is shorter.
def str_compression1(s):
  
  # In order to improve, check ahead of time before generating the compressed string anyways, using the folling three lines of code. 
  # The function count_compression also have quite a few of dup codes as the main function, so it is debatable whehter this is worth.
  
  # final_l = count_compression(s)
  # if final_l > len(s):
  #   return s
  
  result = ""
  count_consecutive = 0
  size = len(s)
  
  for i in range(size):
    count_consecutive += 1
    
    if i+1 == size or s[i] != s[i+1]:
      result += s[i]
      result += str(count_consecutive)
      count_consecutive = 0
 
  return result if len(result) < len(s) else s

def count_compression(s):
  compressed_l = 0
  count_consecutive = 0
  
  size = len(s)
  
  for i in range(size):
    count_consecutive += 1
    
    if i+1 == size or s[i] != s[i+1]:
      compressed_l += 1 + len(str(count_consecutive))
      count_consecutive = 0
  return compressed_l
  
print(str_compression1('aabcccccaaaaaaaaaaaaaaaaaaa'))
print(count_compression('aabcccccaaaaaaaaaaaaaaaaaaa'))

  
print(str_compression1('aab'))
print(count_compression('aab'))

