# Write a function that takes two parameters: (1) an integer N; and, (2) an array of integers.  The function should return a single, uniformly random integer between [0, N-1] such that the resulting integer is NOT one of the integers you are given in the array.

# If it helps, you can assume you have access to a random number generator function called RNG(X) which returns a uniformly random integer between [0, X-1].  However, you don't have to use this RNG function.  For this question, we don't care about space complexity (so, assume everything fits in memory) but we do worry about time complexity (so, the function should run fast).

# An example:
#     N = 10
#     Array = [2, 3, 5]
#     Result = One of 0, 1, 4, 6, 7, 8 or 9 with 1/7 probability.

# Hint: Many candidates will propose a variant of trial-and-error approach: Draw a random number; see if it is in the forbidden list.  If they do, ask them what the time complexity of that approach is.  If they seem to get confused, ask them whether that approach is guaranteed to exit in a finite time.  Finally, push them towards a different solution by asking whether there is a way to solve the question by calling RNG only once.
# Hint: If the first hint doesn't cut it, ask them: "How would you write a function that would return a random number from a given list?".  This is essentially asking how they would implement Python's random.choice() function.  At this point, most candidates will realize that they can "subtract" the forbidden list from a list of [0, N) and get to the solution.
# Hint: Finally, if the second hint doesn't do the trick either, just tell them to compute an "allowed" list and draw a random member from that list.  At this point, the question turns it to "Implement this algorithm" so it is less useful but still provides a signal.  Note that, if the candidate cannot write working code even after this last hint, the candidate is probably not who we are looking for.

import random 

def rand_restr(N, forbidden):
  forb_set = set(forbidden)
  
  allowed=[]
  for i in range(N):
    if i not in forb_set:
      allowed.append(i)
  
  if not allowed:
    raise Exception ("All allowed elements [0, {s}) are forbidden!".format(s=N))
  
  r_ind = random.randint(0,len(allowed)-1)
  return allowed[r_ind]

print(rand_restr(5, [0,1,2,3,4]))

# official
# This is NOT a part of the answer; given here for reference only since
# the existence of such a function is implied in the question.
def RNG(X):
    """The implementation of the RNG as described in the question."""
    assert X >= 0
    return random.randint(0, X - 1) if X >= 1 else 0


# Check to see if the candidate picks "good" names for the function and its
# parameters.  You don't have to "like" the name but many just go with things
# like "foo(n,a)" which is not a good sign.  "N" is universally understood to
# describe a count, a range, etc. so that is fine but what is "a"?
def restricted_randint(N, forbidden):

    # This removes all possible duplicates and makes the lookup in the next
    # loop amortized O(1).  Note that, this is only true if the candidate uses
    # a hash-based container such as set.  A tree-based container will have
    # ~O(logK) time-complexity where K = len(forbidden).  Constructing this
    # container itself takes O(K) time.  Also: Don't let the candidate assume
    # the function takes a set; insist on an array-like container.  We want to
    # see that the candidate explicitly writes the below step.
    forbidden_set = set(forbidden)

    # Candidate might be tempted to pre-allocate memory.  This can only be done
    # if we said forbidden is guaranteed to contain only ints in [0, N-1].
    # Otherwise, pre-allocation becomes tricky.
    allowed = []

    # Time complexity = O(N) but only if forbidden_set is hash-based.
    for i in xrange(0, N):
        if i not in forbidden_set:
            allowed.append(i)

    # Most candidates will miss this edge case.  Ask them afterwards.  Valid
    # answers are throwing an exception or returning something like -1.  Good
    # candidates will give both approaches as possible options.
    if not allowed:
        raise Exception("All numbers [0, %s) are forbidden!" % N)

    # Overall time-complexity of the function at this point: O(N+K)

    r = RNG(len(allowed))
    return allowed[r]

# Official alternative:
# A candidate proficient with Python might write something like below.
# Candidates proficient with R or MATLAB might also come up with similar
# solutions in their corresponding language.  It is very important that you
# ask them the time complexity of each operation in such a case.  Most of
# the time, candidates don't realize how costly some standard function can be.
import random
def my_rand(N, forbidden):
    return random.choice(tuple(set(xrange(0, N)) - set(forbidden)))
