# Given a string S consisting of lowercase English alphabets determine if you can make it a palindrome by removing at most 1 character.

# helper function to decide a string[left:right] is palindrom or not 
def is_palindrom(s, left, right):
  if len(s) <= 1 or left == right:
    return True
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

def is_almost_palindrom(s):
  # corner case that string with 2 characters are alwasy "almost palindrom"
  if len(s) <= 2:
    return True
  left, right = 0, len(s) - 1
  # linear scan string from both ends. If not equal:
  # skip left character to decide string[left+1, right]
  # or skip right charactert to decide string[left, right-1]
  while left < right:
    if s[left] != s[right]:
      return is_palindrom(s, left+1, right) or is_palindrom(s, left, right-1)
    left += 1
    right -= 1
    
print(is_almost_palindrom('abccbd'))
