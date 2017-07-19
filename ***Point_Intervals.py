# Point In Intervals

## Not solved the extention further question... To have the max_s update and calculate in one take...

# Author: Aleksandar Ilic
# Difficulty: Medium

# You are given n integer intervals [a_i, b_i] on the real axes, and the absolute value of the coordinates is bounded by M. Determine a point that belongs to the maximum number of intervals. Point x belongs to the interval [a, b] if a <= x <= b.

# [edit]Naive Solution 

# Traverse all integer points from [-M, M] and check the number of intervals that contain given point. This is very slow solution that runs in O (n * M). One can calculate the leftmost and the rightmost points in order to speedup the algorithm.

# [edit]Better Solution 

# Let A be the point we are looking (this point does not need to be unique). It can be easily shown that there is a point B that belongs to the same number of intervals, where B is either a left or a right end of some interval.

# Therefore, we do not need to traverse all points from [-M, M], but just 2n points that are the left and right ends of intervals. This explains the quadratic algorithm.

# [edit]Optimal Solution 

# We can speedup the above approach, by sorting the intervals from left to right. For example, consider the intervals: [1, 5] [2, 4] [3, 13] [6, 10] [10, 12] [11, 13]

# Engineering--Interviewing--Ninja--Point_In_Intervals--Intervals.png

# If we scan the points from left to right, we get the following numbers of overlapping intervals: 1, 2, 3, 2, 1, 2, 2, 3, 2.

# Notice that when we arrive at left end of some interval - we increase the current number of intervals by 1. Similarly, when arrived at the right end - we decrease the current number of intervals by 1. The special case is when at some coordinate we have both left and right intervals. In that case, first process left ends and then right ends.

# http://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
def points_in_interval(L):
    intervals = []
    n = len(L)
    for i in range(0, n):
        a, b = L[i][0], L[i][1]
        intervals.append((int(a), 1))
        intervals.append((int(b), -1))
    print(intervals)

    intervals.sort(key=lambda i: (i [0], -i [1]))
    print(intervals)
    max_s = 0
    max_p = None
    s = 0
    for pair in intervals:
        s = s + pair[1]
        if s > max_s:
            max_s = s
            max_p = pair[0]
    return max_p

# Extention Extension: Finding maximal ranges 

# If someone solves the first part very quickly, a possible follow-up is finding a list of all the maximal ranges, rather than just a single point.

# For the sample case listed above, the solution would be [ [3, 4], [11, 12] ].

# This doesn't require changing the approach by much; essentially we can update the start when we reach a maximal point and create a range once we reach its endpoint. For example we can use the result of the above solution and add:

def points_in_interval_ext(L):
    intervals = []
    n = len(L)
    for i in range(0, n):
        a, b = L[i][0], L[i][1]
        intervals.append((int(a), 1))
        intervals.append((int(b), -1))
    # print(intervals)

    intervals.sort(key=lambda i: (i [0], -i [1]))
    # print(intervals)
    max_s = 0
    max_p = None
    s = 0
    for pair in intervals:
        s = s + pair[1]
        if s > max_s:
            max_s = s
            max_p = pair[0]
    
    s = 0
    max_range=[]
    start = None
    
    for pair in intervals:
      s += pair[1]
      if s == max_s:
        start = pair[0]
      elif start is not None:
        max_range.append([start, pair[0]])
        start = None
    return max_range
    

print(points_in_interval([[1,4],[2,5],[10,12],[5,9],[5,12]]))
print(points_in_interval([[1,5], [2,4], [3,13], [6,10], [10,12], [11,13]]))

print(points_in_interval_ext([[1,4],[2,5],[10,12],[5,9],[5,12]]))
print(points_in_interval_ext([[1,5], [2,4], [3,13], [6,10], [10,12], [11,13]]))

### Extention further:
# To mix it up even further, you can then ask for a 1-pass variation on the above solution that updates/calculates max_s at the same time.

# [edit]Typical problems/discussion 

# If M is small, one can use counting sort and get time complexity O (M + n).
# What about the same problem in 2 dimensions?
# The problem can be formulated as time intervals, with an additional processing of timestamps like '2:22:22 PM  2:22:33 PM'
# What about if intervals have weights, and you need to find a point with maximum weight (just use weights instead of +/-1).
# One can also use interval trees data structure in order to efficiently determine whether a given point belongs to an interval.

