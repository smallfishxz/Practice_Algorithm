def get_category(n):
  if n <= 10 and n > 0:
    return 'LOW'
  elif n <= 20:
    return 'MEDIUM'
  elif n > 20:
    return 'HIGH'

# two passes, extra space    
def dutch_flag1(A):
  buckets = {'LOW': [], 'MEDIUM': [], 'HIGH': []}
  for i in range(len(A)):
    buckets[get_category(A[i])].append(A[i])
  return buckets['LOW'] + buckets['MEDIUM'] + buckets['HIGH']

# two passes, extra spaces
def dutch_flag2(A):
  count = {'LOW': 0, 'MEDIUM': 0, 'HIGH': 0}
  
  for item in A:
    count[get_category(item)] += 1
  
  indices = {'LOW': 0, 'MEDIUM': count['LOW'], 'HIGH': count['LOW'] + count['MEDIUM']}
  B = [0 for i in range(len(A))]
  for item in A:
    t = get_category(item)
    B[indices[t]] = item
    indices[t] += 1
  return B

# one pass, no extra space
# Reference: https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem
def dutch_flag3(A):
  l_idx = 0
  h_idx = len(A) - 1
  m_idx = 0

  while (m_idx <= h_idx):
    t = get_category(A[m_idx])
    
    if t == 'LOW':
      A[l_idx], A[m_idx] = A[m_idx], A[l_idx]
      l_idx += 1
      m_idx += 1
    if t == 'MEDIUM':
      m_idx += 1
    if t == 'HIGH':
      A[h_idx], A[m_idx] = A[m_idx], A[h_idx]
      h_idx -= 1
  return A
  
print(dutch_flag3([5,32,2,12,27,19,14]))
