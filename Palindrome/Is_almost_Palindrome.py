def ispalindrome(s, start, end):
  while start < end:
    if s[start] != s[end]:
      return False
    start += 1
    end -= 1
  
  return True

def isalmostpalindrome(s):
  i, j = 0, len(s)-1
  while i < j:
    if s[i] != s[j]:
      return ispalindrome(s, i+1, j) or ispalindrome(s, i, j-1)
    i += 1
    j -= 1
  
  return True  

print(isalmostpalindrome('abccd'))

# len = 1 is handled well by the last line in main function
# len = 2 like aa, is also handled by last line in main function
# len = 2 like ab, is handled last line in the sub-function
# So there is no need to handle any edge cases in the code.
