def fib(n):
    result = 0
    if n == 0:
        result
    elif n == 1:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


print(fib(6))
