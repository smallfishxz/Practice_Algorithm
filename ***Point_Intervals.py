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
    
    
print(points_in_interval([[1,4],[2,5],[10,12],[5,9],[5,12]]))
print(points_in_interval([[1,5], [2,4], [3,13], [6,10], [10,12], [11,13]]))
