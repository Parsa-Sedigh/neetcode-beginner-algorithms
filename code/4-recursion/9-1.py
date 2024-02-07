# Recursive implementation of n! (n-factorial) calculation
# Time: O(n)
# Space: O(n)
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

# non recursive solution
# Time: O(n)
# Space: O(1)
def factorialIterative(n):
    res = 1

    while n > 1:
        res = res * n
        n -= 1

    return res