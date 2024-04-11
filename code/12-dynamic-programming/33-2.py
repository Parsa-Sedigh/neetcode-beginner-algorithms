def fibonacci_with_memoization(n, cache):
    if n <= 1:
        return 1

    # O(1). If cache was an arr, we know the index and we would get it instantly. So it would be O(1) as well since
    # we know which index to look. How? For example when calculating f(2), we put the result in index = 2.
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)

    return cache[n]

print(memoization(5, {}))