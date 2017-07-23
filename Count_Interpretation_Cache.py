# Cache reference: https://codereview.stackexchange.com/a/95556

# Improving time complexity
# The first simple improvement is to note that there are a lot of repeated computations and to store the result of a subproblem in a cache 
# (aka. "memoization") and to look that up before calling the function recursively.
# This reduces the time complexity from exponential to linear since we need to compute the result for a specific subproblem only once.
# The space complexity is still linear, but we have used O(n) extra space.

def find_count(A, pos, cache):
    if pos in cache:
      return cache[pos]
    
    ll = len(A)
    
    if pos==ll:
        return 1
    
    if A[pos]=='0':
        return 0
    
    if pos==ll-1:
        return 1
    
    count=find_count(A, pos+1, cache)
    
    if int(A[pos:pos+2])<=26:
        count+=find_count(A, pos+2, cache)
    
    cache[pos] = count
    print(cache)
    return count

print(find_count('111', 0, {}))
