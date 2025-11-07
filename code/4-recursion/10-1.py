# Recursive implementation to calculate the n-th Fibonacci number
# time: O(2^n)
# space: O(n)
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 1)
    return fibonacci(n - 1) + fibonacci(n - 2)

# T: O(n)
# M: O(1)
# 0,1,1,2,3,5,8,13,21,34
def fibonacci_iterative(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    # Start with the first two values
    a, b = 0, 1

    # Build up from 2 to n
    for i in range(2, n+1):
        a, b = b, a + b # next = prev + curr; shift

    return b