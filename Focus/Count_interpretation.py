# special case for digit arr starts with '0'
# abX have two ways in total to interprate:
# case 1: a, bx
# case 2: as long as ab between 10 and 26: ab, x

# Note: have to put size == 0 at the beginning, otherwise, will run into out of index error.

# Similar to Fibonacci problem, n problem has two sub problems n-1 and n-2 to solve, so time complexity is 2^n, and space complexity is O(n) (linear for recursive algo and depth of stack is O(n))

def count_interpretation(arr):
  size = len(arr)
  
  # Base case and also special case for empty digit string
  if size == 0:
    return 1
  
  # if digit array starts with '0', no valid interpretation. count is 0
  if arr[0] == '0':
    return 0

  # base case. if single digit array, count is 1
  if size == 1:
    return 1

  # if digit array doesn't start with '0', consider to interpretation like (first digit, arr[1,n]). so recursively interprate arr[1,n].
  # case 1: to interprete as a, bX
  count = count_interpretation(arr[1:size])
  
  # if first two digits in the array is between 10 and 26, then arr could have another way to interprate as (first 2 digits, arr[2:n]). so recursively interprete arr[2:n], and add them to case 1 interpretation
  # case 2: to interprate as ab, X
  if int(arr[0:2]) >= 10 and int(arr[0:2]) <= 26:
    count += count_interpretation(arr[2:size])
  
  return count

def count_interpretation_cache(arr, index, cache):
  if index in cache:
    return cache[index]
  
  size = len(arr)
  if index == size:
    count = 1
  elif arr[index] == '0':
    count = 0
  elif index == size - 1:
    count = 1
  else:
    count = count_interpretation_cache(arr, index+1, cache)
    if int(arr[index:index+2]) >=10 and int(arr[index:index+2]) <= 26:
      count += count_interpretation_cache(arr, index+2, cache)
  
  cache[index] = count
  print(cache)
  return count    
  
print(count_interpretation_cache('111', 0, {}))
