Write a function that takes two parameters: (1) an integer N; and, (2) an array of integers.  The function should return a single, uniformly random integer between [0, N-1] such that the resulting integer is NOT one of the integers you are given in the array.

If it helps, you can assume you have access to a random number generator function called RNG(X) which returns a uniformly random integer between [0, X-1].  However, you don't have to use this RNG function.  For this question, we don't care about space complexity (so, assume everything fits in memory) but we do worry about time complexity (so, the function should run fast).

An example:
    N = 10
    Array = [2, 3, 5]
    Result = One of 0, 1, 4, 6, 7, 8 or 9 with 1/7 probability.




If the candidate gets stuck, you can progressively give the following hints in the order they appear:

Hint: Many candidates will propose a variant of trial-and-error approach: Draw a random number; see if it is in the forbidden list.  If they do, ask them what the time complexity of that approach is.  If they seem to get confused, ask them whether that approach is guaranteed to exit in a finite time.  Finally, push them towards a different solution by asking whether there is a way to solve the question by calling RNG only once.
Hint: If the first hint doesn't cut it, ask them: "How would you write a function that would return a random number from a given list?".  This is essentially asking how they would implement Python's random.choice() function.  At this point, most candidates will realize that they can "subtract" the forbidden list from a list of [0, N) and get to the solution.
Hint: Finally, if the second hint doesn't do the trick either, just tell them to compute an "allowed" list and draw a random member from that list.  At this point, the question turns it to "Implement this algorithm" so it is less useful but still provides a signal.  Note that, if the candidate cannot write working code even after this last hint, the candidate is probably not who we are looking for.

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
