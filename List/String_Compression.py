# Iterate through the string char by char, and count its repeats. When next char is not the same as the current one, append the char and its repeats to the result string.
# In the end return the result string only when it is shorter.
def str_compression1(s):
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
  
print(str_compression1('aabcccccaaa'))
