def fibo_brute_force(n):
    if n <= 1:
        return 1

    return fibo_brute_force(n - 1) + fibo_brute_force(n - 2)

print(fibo_brute_force(5))