# Target

# This question tests basic algorithmic and programming skills, complexity analysis, and ability to optimize for time and space.

# [edit]Question

# We have a coding system from letters to numbers where a=1, b=2, ...z=26. You are given a string of digits as an input. Write a function that will compute the number of valid interpretations of the input.

# [edit]Setting up the question

# Examples: 
# f('11') = 2 Actual interpretations: ('aa', 'k') 
# f('111') = 3 Actual interpretations: ('aaa', 'ak', 'ka') 

# You can tell them that the expected answer for '11' should be 2 and ask them what the answer should be for '111' or for some other small input.

# Repeat to the candidate that the goal is to just output the count and not necessarily all the valid interpretations as strings.

# [edit]Solution 1

# The problem lends itself to a simple recursive solution. Assume the given string S is of the form abX where a and b are single digits and X is the rest of the string.

# Anything that start's with a zero cannot have a valid interpretation since there is no valid character that 0 maps to. So the answer for any string that starts with a zero is 0.

# Case 1: If a is a digit from 1-9, it can represent some character from [a-i] 
# Case 2: If ab taken together has a value from 10-26, it can represent some character from [j-z] 

# Since these two cases are mutually exclusive, the number of possible interpretations of abX = number of possible interpretations of bX (Case 1) + number of possible interpretations of X (Case 2).

def find_count(A):
    ll=len(A)
    if ll==0:
        return 1
    
    if A[0]=='0':
        return 0
    
    if ll==1:
        return 1
    
    count=find_count(A[1:ll])
    
    if int(A[0:2])<=26:
        count+=find_count(A[2:ll])
    
    return count

print(find_count('11'))

# Edge cases: Zero needs to be handled specially as shown in the code above. This surprisingly trips up a few people. Make sure the candidate realizes that and has a reasonable solution for it. It shows capability for attention to detail. If the candidate has the basic structure right and ends up spending too much time in the corner cases, I usually just go to the complexity analysis (see next section) and come back to this at the end.

# Gotchas: I've seen several people add an extra 1 to the formula as in $count = 1 + countPerms($num, 1, $len - 1); This is wrong. If you ask them to run their algorithm on a small input, they should realize the mistake quickly.

# [edit]Complexity Analysis

# Time complexity: Exponential. Roughly O(2^n) since for a string of length n, we have 2 sub-problems of size n-1 & n-2. Strictly speaking, the complexity is fibonacci(n) since the recurrence relation for the worst case is exactly the fibonacci sequence.

# Space Complexity: Linear. Since it is recursive and depth of stack is O(n)
