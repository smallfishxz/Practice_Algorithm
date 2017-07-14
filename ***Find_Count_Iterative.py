def find_count_iterative(A):
    pos, ll=len(A)-1, len(A)
    # count_curr, count_prev and count_prev2 represent the number of interpretations 
    # of the substrings starting at position x, x+1 and x+2 respectively.
    count_curr = 0
    count_prev, count_prev2 = 1,1
    while pos >= 0:
        if A[pos]=='0':
            count_curr = 0
        else:
            count_curr = count_prev
            if pos + 2 <= ll and int(A[pos:pos+2]) <= 26:
                count_curr += count_prev2
        count_prev2 = count_prev;
        count_prev = count_curr
        pos-=1
    return count_curr

print find_count_iterative('111')

# function countPerms($num) {
#   $len = $pos = strlen($num);

#   // count_curr, count_prev and count_prev2 represent the number of interpretations 
#   // of the substrings starting at position x, x+1 and x+2 respectively.
#   $count_curr = 0;
#   $count_prev = $count_prev2 = 1; // counts start at 1 (they're only added if valid)

#   while (--$pos >= 0) {
#     if ($num[$pos] === '0') {
#       // Any string starting with '0' has no valid interpretation
#       $count_curr = 0;
#     } else {
#       $count_curr = $count_prev;

#       if ($pos + 2 <= $len && intVal(substr($num, $pos, 2)) <= 26) {
#         $count_curr += $count_prev2;
#       }
#     }

#     $count_prev2 = $count_prev;
#     $count_prev = $count_curr;
#   }

#   return $count_curr;
# }
