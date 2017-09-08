# Question: Determine if any 3 integers in an array sum to 0.

# allow repetivive pick 
# brute force, time complexity O(N*N*N)
def find_3_sum_zero_bf(A):
  size = len(A)
  for i in range(size):
    for j in range(i, size):
      for k in range(j, size):
        if A[i] + A[j] + A[k] == 0:
          print(A[i], A[j], A[k])

# Optimize the inner loop
# allow repetivive pick 
# brute force, time complexity O(N*N*N)
def find_3_sum_zero_bf1(A):
  size = len(A)
  for i in range(size):
    for j in range(i+1, size):
      for k in range(j+1, size):
        if A[i] + A[j] + A[k] == 0:
          print(A[i], A[j], A[k])

# Allow repetitive pick
# Hash table to find the third element. O(N*N) and space is O(N)
# Allow repetitive pick
def hashtable_soln(A):
  dic = {}
  size = len(A)
  for i in range(size):
    # hash value is the last occurency index of key element
    dic[A[i]] = i
  # print(dic)
  for i in range(size):
    for j in range(i, size):
      sum = -(A[i] + A[j])
      # print(i, j, sum)
      if sum in dic.keys() and j <= dic[sum]:
        print(A[i], A[j], sum)

# not allow repetitive pick
def find_3_sum_zero(A):
  dic = {}
  size = len(A)
  for i in range(size):
    # hash value is the last occurency index of key element
    dic[A[i]] = i
  # print(dic)
  for i in range(size):
    for j in range(i+1, size):
      sum = -(A[i] + A[j])
      # print(i, j, sum)
      # if sum in dic and i != dic[sum] and j != dic[sum]:
      if sum in dic.keys() and j < dic[sum]:
        print(A[i], A[j], sum)

# O(n^2) solution that does not require extra space. Sorted the array
# allowed repetitive pick
# Loop through each element, and try to find a pair of elements with sum as -element
def find_3_sum_zero2(A):
  sorted(A)
  size = len(A)
  for i in range(size):
    l = i
    r = size-1
    while l <= r:
      if A[l] + A[r] == -A[i]:
        print(A[i], A[l], A[r])
        break
      elif A[l] + A[r] < -A[i]:
        l = l+1
      else:
        r = r-1
# not allow repetitive pick
def find_3_sum_zero3(A):
  sorted(A)
  size = len(A)
  for i in range(size):
    l = i+1
    r = size-1
    while l <= r:
      if A[l] + A[r] == -A[i]:
        print(A[i], A[l], A[r])
        break
      elif A[l] + A[r] < -A[i]:
        l = l+1
      else:
        r = r-1

# find_3_sum_zero_bf1([-1,0,1])
# hashtable_soln([-1,0,1])
find_3_sum_zero3([-1,0,1]


