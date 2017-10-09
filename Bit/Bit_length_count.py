# return the length of binary representation, and the count of bit 1

def bit_length_count(num):
  size = 0
  count = 0
  while num:
    size += 1
    count += num&1
    num >>=1
  return (size, count)

print(bit_length_count(2))
