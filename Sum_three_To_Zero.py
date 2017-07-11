# Question: Determine if any 3 integers in an array sum to 0.

def brute_force2(arr):
    for i in range(0, len(arr)):
        for j in range (i, len(arr)):
            for k in range(j, len(arr)):
                if ((arr[i] + arr[j] + arr[k]) == 0):
                    print(arr[i], arr[j], arr[k])

# dont allow repetitive pick
def hashtable_soln(arr):
    # create hashtable and insert all values in array
    vals = {}
    for i in range(len(arr)):
      vals[arr[i]] = i
    for i in range(len(arr)):
      for j in range(i + 1, len(arr)):
        sum = -(arr[i] + arr[j])
        # Note: this will print out the same solution multiple times. For instance,
        # [0,-1,1] will print 3 solutions. To print only unique solutions:
        # if vals.has_key(sum) and j < vals[sum]:
        # if sum in vals and i != vals[sum] and j != vals[sum]:
        if sum in vals and j<vals[sum]:
          print(arr[i], arr[j], sum)

# dont allow repetitive pick and require no extra space
def hashtable_soln_imp(A):
  A=sorted(A)
  for i, s in enumerate(A):
    # if allow repetitive pick, min_index=i
    min_index = i+1
    max_index=len(A)-1
    while (min_index<=max_index):
      if A[min_index]+A[max_index]>-s:
        max_index-=1
      elif A[min_index]+A[max_index]<-s:
        min_index+=1
      else:
        print(A[i], A[min_index],A[max_index])
        break


# allow repetitive pick
def hashtable_soln1(arr):
    # create hashtable and insert all values in array
    vals = {}
    for i in range(len(arr)):
      vals[arr[i]] = i
    for i in range(len(arr)):
      for j in range(len(arr)):
        sum = -(arr[i] + arr[j])
        # Note: this will print out the same solution multiple times. For instance,
        # [0,-1,1] will print 3 solutions. To print only unique solutions:
        # if vals.has_key(sum) and j < vals[sum]:
        if sum in vals:
          print(arr[i], arr[j], sum)

print( hashtable_soln_imp([0,-1,1]))


