# permutation of palindrome has at most 1 odd number of char, other chars need to be with even numbers
def permutation_palindrome(s):
  dic = dict()
  for c in s:
    low_c = c.lower()
    if low_c.isalpha():
      if low_c not in dic:
        dic[low_c] = 1
      else:
        dic[low_c] += 1
  
  print(dic)
  
  find_odd = False
  for v in dic.values():
    if v % 2 == 1:
      if find_odd == True:
        return False
      else: 
        find_odd = True
  
  return True
