# Cache reference: https://codereview.stackexchange.com/a/95556

cache={}
pos=0
def find_count(A, pos):
    ll = len(A)-pos
    
    if ll==0:
        return 1
    
    if A[0]=='0':
        return 0
    
    if ll==1:
        return 1
    
    count=find_count(A[pos+1:ll], pos)
    
    if int(A[pos:pos+2])<=26:
        count+=find_count(A[pos+2:ll], pos)
    return count

def find_count_m(A):
    if pos not in cache:
        cache[pos]=find_count(A, pos)
    return cache[pos]

print find_count_m('21')
