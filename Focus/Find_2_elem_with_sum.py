# Is sorted array? dup elements allowed? negative numbers?
# test case should also include: single elments, empty array 

# O(n*n)
def solution(input, sum):
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            if (input[i] + input[j] == sum):
                return True
    return False

# O(N * log N)
def solution2(input, sum):
    sorted(input)
    i = 0
    j = len(input) - 1
    
    while (i < j):
        total = input[i] + input[j]
        if (total == sum):
            return True
        elif (total > sum):
            j=j-1
        elif (total < sum):
            i=i+1
    return False

# O(N). Build and search the dictionary while looping through the array
def find_elems_with_sum(A, sum):
  dic = {}
  for elem in A:
    # if (sum - elem) in dic.keys():
    if dic.get(sum-elem):
      return True
    dic[elem] = True
    print(dic)
  
  return False

# O(N). dictionary is not quite necessay, could replace dictionary with a set
def find_elems_with_sum1(A, sum):
  s = set()
  for item in A:
    if (sum - item) in s:
      return True
    s.add(item)
  return False
      

print(find_elems_with_sum1([1,2,4], 6))
    
