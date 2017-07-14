cache = {}
def fibonacci(n):
    if n<=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def memo_f(n):
    if n not in cache:
        cache[n] = fibonacci(n)
    return cache[n]

print memo_f(2)
