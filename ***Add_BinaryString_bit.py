def add(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            x_bit = x[i] & 1
            y_bit = y[i] & 1
            


        return result.zfill(maxlen)
        # return result

print add_0('1','111')        
print add('1','111')}

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
