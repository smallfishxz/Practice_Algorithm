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
