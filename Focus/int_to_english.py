
# 2**10 ~ 1k, 2**20 ~ 1M, 2**30 ~1B, 2**31 ~2b, leave one bit for signed
# 32 bit could represent -2B to 2B number.

# 1-19 is specially spelled out
# we leave out 'zero' as for number as 30, we don't want to spell out as thirty zero
# Also it is good to leave out empty for the first element as index 0, as it will make the following mapping easier
NUMBERS = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

# tens numbers are also specially spelled out
# same thing to leave out the first two elements empty, to make the following mapping easier
TENS = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

# handling triplets in a sub-function
def triple_to_english(num):
  print(num)
  e_str = []
  if num >= 100:
    e_str.append(NUMBERS[num//100])
    e_str.append('hundred')
    num = num%100
  # for triple digits, 20 is a threshold to divide into two cases
  if num < 20:
    e_str.append(NUMBERS[num])
  else:
    e_str.append(TENS[num//10])
    e_str.append(NUMBERS[num%10])
    
  return ' '.join(e_str)


def int_to_english(num):
  # 0 is edge case to specially handle
  if num == 0:
   return('zero')

  e_str = []
  # minus number is also a speical case to handle
  if num < 0:
    num *= -1
    e_str.append('minus')
  if num >= 1000000000:
    e_str.append(triple_to_english(num//1000000000))
    e_str.append('billion')
    num = num%1000000000
  if num >= 1000000:
    e_str.append(triple_to_english(num//1000000))
    e_str.append('million')
    num = num%1000000
  if num >= 1000:
    print('>=1000 condition')
    e_str.append(triple_to_english(num//1000))
    e_str.append('thousand')
    num = num%1000
  if num >= 0: 
    e_str.append(triple_to_english(num))
  
  return ' '.join(e_str)

print(int_to_english(-676542321000))
