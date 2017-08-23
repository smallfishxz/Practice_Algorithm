# x = bottl, y = ewater, 
# s1 = xy = bottlewater, s2= yx = ewaterbottl
# s2 - yx  must be a substring of s1s1 = xyxy

def is_rotation(s1, s2):
  size = len(s1)
  
  if len(s2) == size and size > 0:
    s1s1 = s1 + s1
    print(s1s1)
    return True if s1s1.find(s2) >= 0 else False 
  
  return False
  

print(is_rotation('bottlewater', 'ewaterbottl'))
