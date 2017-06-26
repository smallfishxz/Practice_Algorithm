def add(x,y):
#         Iterate till there is no carry
        while y != 0:
#                 carry now contains common set bits of x and y
                carry = x & y
#         sum of bits of x and y where at least one of the bits is not set
                x = x ^ y
#         carry is shifted by one so that adding it to x gives the required sum
                y = carry << 1
        return x
        

# unsigned int add_slow(unsigned int i, unsigned int j) {
#  unsigned result = 0;
#  unsigned mask = 1;
#  unsigned carry = 0;
#  while (i | j | carry)  {
#     unsigned ibit = i & 1;
#     unsigned jbit = j & 1;
#     unsigned sum = carry ^ ibit ^ jbit;
#     carry = carry&ibit | carry&jbit | ibit&jbit;
#     result |= sum ? mask : 0;
#     mask <<= 1;
#     i >>= 1;
#     j >>= 1;
#  }
#  return result;
#}
