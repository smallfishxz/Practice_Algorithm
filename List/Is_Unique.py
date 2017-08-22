def is_unique(s):
  char_set = set()
  
  for c in s:
    if c not in char_set:
      char_set.add(c)
    else:
      return False
  
  return True

def is_unique2(s):
  size = len(s)
  for i in range(size):
    for j in range(i+1, size):
      if s[i] == s[j]:
        return False
  return True


print(is_unique2('ababd'))
