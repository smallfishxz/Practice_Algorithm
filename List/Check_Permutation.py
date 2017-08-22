# ABC permutation strings are: ACB, BAC, BCA, CAB, CBA

def is_permutation(s1, s2):
  if len(s1) != len(s2):
    return False
  
  s1_sort = ''.join(sorted(s1))
  s2_sort = ''.join(sorted(s2))
  
  return s1_sort == s2_sort
  
def is_permutation2(s1, s2):
  if len(s1) != len(s2):
    return False
  
  dic = dict()
  for c in s1:
    if c not in dic:
      dic[c] = 1
    else:
      dic[c] += 1
  
  for c in s2:
    dic[c] -= 1
    if dic[c] < 0:
      return False
  
  return True
  

print(is_permutation2('ababd', 'abdad'))
