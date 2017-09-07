# differ

# Solution one is looking to find the first bad via the first variable
# Input parameters is the range within which the first bad was introduced. 
# Move the first and last around to shrink the search range for the first bad till nailing down the first bad.
def find_bisect(first, last):
  first += 1
  while first <= last:
    mid = first + (last - first)//2
    if isbad(mid):
      last = mid
    else:
      first = mid + 1
   
  return first

# solution 2 is looking to find the first bad via the bad variable
# Input parameters are a wider range with good and bad blame revisions. Whenever there is revision between good and bad
# there is chance that bad revision happens before current bad. 
# So to exit the loop, search until good revision's next is a bad, then return bad.
def find_bisect1(good, bad):
  while good < bad - 1:
    mid = good + (bad - good)//2
    if isbad(mid):
      bad = mid
    else:
      good = mid
   
  return bad
      
  
