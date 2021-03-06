# linear scan starting from 0 to get the quotient and reminder
# the key to exit loop is when num - div*q >=0 or num - div*q >= div
# then quotient is q-1 or q
def divide(num, div):
  assert (div == 0), "div is 0!"
  q = 0
  while num - div*q >= 0:
    q += 1
  return (q-1, num - div*(q-1))

# binary search between 0 to num (the possible range of the quotient) to get the quotient and reminder
# if reminder < 0, means the div is too big, and it should be within the lower part
# if reminder >= div, means the div is too small, and it should be within the upper part
# So to exit the loop, reminder >=0 or reminder < div
# Also as cannot divide, so using the bit manipulation to get the //. 5>>1 vs. 5//2
def divide2(num, div):
  l = 0
  h = num
  mid = (l+h) >> 1
  reminder = num - div*mid
  
  # while not (reminder >= 0 and reminder < div):
  while reminder < 0 or reminder >= div:
    if reminder < 0:
      h = mid
    else:
      l = mid
    mid = (l+h) >> 1
    reminder = num - div*mid 
  
  return (mid, reminder)
    

print(divide2(7, 5))
