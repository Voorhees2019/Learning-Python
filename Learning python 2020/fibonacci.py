def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))


def fibonacci2(n):
    fib1, fib2 = 1, 1
    print(fib1, end=' ')
    print(fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


fibonacci2(5)
