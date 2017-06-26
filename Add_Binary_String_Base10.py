def add(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            digit_x = int(x[i]) - int('0')
            digit_y = int(y[i]) - int('0')
            r = r + digit_x + digit_y
            
            # r can be 0 to 19 (carry + x[i] + y[i])
            # and among these, 
            # for r==10 to r==19 you will have result bit = r-10, carry = 1
            # for r==0 and r==9 you will have reult bit = r, carry = 0
            
            if r >= 10 and r <= 19:
              result = str(r-10) + result
              carry = 1
            elif r >=0 and r <= 9:
              result = str(r) + result
              carry = 0

        if carry !=0 : result = '1' + result

        return result.zfill(maxlen)
        # return result

print add('123','111')        
# print add('999','111')
