def b_search(A, n):
    l=0
    r=len(A)-1
    while l<=r:
        mid = (l+r)//2
        if A[mid]==n:
            return mid
        elif A[mid]<n:
            l=mid+1
        else:
            r=mid-1
    return -1

print(b_search([2,3,4,10,40], 10))
