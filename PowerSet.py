# Reference: http://www.geeksforgeeks.org/power-set/
# time complexity: O(n*2**n)
def powerset_iterative(items):
  ll = len(items)
  result=[]
  # loop through 000...000 to 111...111
  for i in range(2**ll):
    bucket = []
    # for every element in items
    for j in range(ll):
      # check the jth element of items is picked or not
      if i & (1<<j):
        bucket.append(items[j])
    result.append(bucket)
  return result

# Reference: http://www.ecst.csuchico.edu/~akeuneke/foo/csci356/notes/ch1/solutions/recursionSol.html
# p([1,2,3]) = p([2,3])+ ([1] union every element in p([2,3]))
# time complexity: O(2**n)
def p(l):
    if not l: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]
  
# print(powerset_iterative([1,2,3]))
# print(p([1,2,3]))

# print([[1]+[2]])

# Python iterator/generator implementation reference: https://stackoverflow.com/a/24377
# reference2: http://anandology.com/python-practice-book/iterators.html
class Counter:
  def __init__(self, low, high):
    self.current = low
    self.high = high

  def __iter__(self):
    return self

  def __next__(self): # Python 3: def __next__(self)
    if self.current > self.high:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1

for c in Counter(3, 8):
    print(c)
