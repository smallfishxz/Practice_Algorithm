def reverse_str(s):
  return s[::-1]
  
def reverse_str2(s):
  return(''.join(reversed(s)))

def reverse_str3(s):
  return (''.join(sorted(s, reverse=True)))
  
  
print(reverse_str('abc'))
print(reverse_str2('abc'))
print(reverse_str3('abc'))
