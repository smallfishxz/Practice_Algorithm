# reference: https://leetcode.com/problems/hamming-distance/discuss/
def hamming_distance(a,b):
  return bin(a^b).count('1')

# reference: https://en.wikipedia.org/wiki/Hamming_distance
# O(logM), M is the larger number between a and b
def hamming_distance1(a,b):
  s = 0
  x = a^b
  print(x)
  # Count the number of bits set
  while x > 0:
    # one bit is set, so increment and clear the bit
    s += 1
    print("{}&{} is {}".format(x, x-1, x&(x-1)))
    x &= (x-1)
  return s
    
# print(hamming_distance1(1,4))


def sum_hamming_distance(A):
  ll = len(A)
  s = 0
  for i in range(ll):
    for j in range(i+1, ll):
      s += bin(A[i]^A[j]).count('1')
  return s

# O(n*n*logM), M is the larget number among elements in A
def sum_hamming_distance1(A):
  ll = len(A)
  s = 0
  for i in range(ll):
    for j in range(i+1, ll):
      x = A[i]^A[j]
      while x > 0:
        s += 1
        x &= (x-1)
  return s

# Reference: http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/, but the calculation is not accurate,
# should get rid of *2 but just keep count*(n-count)
# O(n*logM),M is the lagest number among elements in A
def sum_hamming_distance2(A):
  ll = len(A)
  s = 0
  # each ele in A is representing by a 32 bit binary number. Loop through each bit of the 32 bits
  for i in range(32):
    # loop through each element under ith bit
    count = 0
    for j in range(ll):
      if (A[j] & (1 << i)):
        # count the number of elements in A that ith bit is set
        count += 1
    s += count * (ll-count)
  return s

print(sum_hamming_distance2([1,4,5]))
