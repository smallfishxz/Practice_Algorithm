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

# Potential optimization to avoid a full scan on the dictionary, but not necessarily optimal as there is extra work to do for each step in the loop
def permutation_palindrome1(s):
  dic = dict()
  count_odd = 0
  for c in s:
    low_c = c.lower()
    if low_c.isalpha():
      if low_c not in dic:
        dic[low_c] = 1
      else:
        dic[low_c] += 1
      
      if dic[low_c] % 2 == 1:
        count_odd += 1
      else:
        count_odd -= 1
  
  return count_odd <= 1
      
print(permutation_palindrome1('Tact Cob'))

