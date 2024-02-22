# Recursive implementation to calculate the n-th Fibonacci number
# time: O(2^n)
# space: O(n)
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 1)
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciIterative(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

# n is the number of TERMS in the sequence
def printFibonacciIterative(n):
    a, b = 0, 1

    print(a, b)

    while n - 2:
        a, b = b, a + b
        print(a + b)

        n -= 1

    return a