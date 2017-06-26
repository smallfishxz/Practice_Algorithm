# http://campuscoke.blogspot.com/2014/12/add-two-numbers-without-using.html

def add(a,b):
        while (1): 
                sum = a ^ b
                carry = a & b
                carry = carry << 1
                if carry == 0:
                        break
                else:
                        a = sum
                        b = carry
        return sum
        
# alternative: http://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
def add (a,b):
        while (b != 0):
                carry = a & b
                a = a ^ b
                b = carry << 1
        
        
# official answer
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
