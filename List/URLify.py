def replace_blank(s, n):
  tmp = s.rstrip().replace(" ", "%20")
  return tmp

def replace_blank2(s, n):
  tmp = '%20'.join(s.rstrip().split(" "))
  return tmp

# Below is a solution in Java, but will fail to run for Python as python string doesn't does not support item assignment 
# def replace_blank3(s, true_l):
#   space_count = 0
#   for i in range(true_l):
#     if s[i] == ' ':
#       space_count += 1
  
#   index = true_l + space_count * 2

#   for i in range(true_l-1, -1, -1):
#     if s[i] == ' ':
#       s[index - 1] = '0'
#       s[index - 2] = '2'
#       s[index - 3] = '%'
#       index -= 3
#     else:
#       s[index - 1] = s[i]
#       index -= 1
 
#   return s

s1 = "Mr John Smith    "
print(replace_blank2(s1, 13))
