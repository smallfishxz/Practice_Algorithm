def sort_per_alphabet(s, alpha):
  
  l = list(s)
  l.sort(key = lambda c: alpha.index(c))
  return ''.join(l)

def sort_per_alphabet2(s, alpha):
  dic = {}
  dic2 = {}
  result = []
  for c in s:
    if c in alpha:
      if c not in dic:
        dic[c] = 1
      else:
        dic[c] += 1
    else:
      if c not in dic2:
        dic2[c] = 1
      else:
        dic2[c] += 1
  
  for c in alpha:
    num = dic[c]
    for i in range(num):
      result.append(c)
  
  for k in dic2:
    v = dic2[k]
    for i in range(v):
      result.append(k)
  
  return ''.join(result)

def sort_per_alphabet3(para, alpha):
  para.sort(key = lambda word: [alpha.index(c) for c in word])
  return para
  
print(sort_per_alphabet2('abcfaeb', 'bca'))
print(sort_per_alphabet3(['af', 'ax', 'am', 'ab', 'zvpmf'], "bafmxpzv"))
