# decide whether an integer is a Palindrom.

def is_palindrom(num):
  if num < 0:
    return False
  copy, reverse = num, 0
  while copy:
    reverse *= 10
    reverse += copy%10
    copy //= 10
  return reverse == num

print(is_palindrom(123321))
