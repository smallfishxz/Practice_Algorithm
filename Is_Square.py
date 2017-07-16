# A perfect square is an integer that is the product of an integer multiplied by itself. i.e. n**2 for any integer n. e.g. [0, 1, 4, 9, 16, 25 . . .].

# Write a function that takes an integer and returns True if the integer is a perfect square, and False otherwise.
# Write the same function without using the square root function. What's the runtime of that solution (using big-oh notation)?
# Improve the runtime of that function.
# What's the best we could do? i.e. how do you think sqrt is implemented? 


# A good candidate will write, in this order: O(n), O(sqrt(n)), O(log(n)) solutions, although it may take some leading to get them to realize that without recourse to numerical trickiness, this is basically a search problem over a sorted range, and therefore amenable to a modified binary search. Bonus points for numerical trickiness (e.g. Newton-Raphson, knowledge of Carmack's hack), but those things are totally not expected.

# There are a spectrum of answers, which I've attempted to capture below.

# O(n)
def is_square_0(n):
  for i in range(n):
    square = i*i # worry about overflow
    if square == n:
      return True
  return False

# O(sqrt(n))
def perfect_square(n):
  i = 0
  while (i*i<n):
    i+=1
  if i*i==n:
    return True
  elif i*i>n:
    return False

# O(logn)
def perfect_square_1(n):
  low=0
  high=n-1
  while low<=high:
    mid=(low+high)//2
    print (mid)
    square=mid*mid
    if square==n:
      return True
    elif square<n:
      low=mid+1
    else:
      high=mid-1
  return False

# O(sqrt(n))
def is_square(n):
  for i in range(n):
    square = i*i # worry about overflow
    if square == n:
      return True
    if square > n:
      return False
  return False

# print(perfect_square_1(9))
print(is_square(7))
