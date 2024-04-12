# Brute Force - DFS
# Time: O(2 ^ (n + m))
# Space: O(n + m)
# Note: We can't ever go out of bounds in the way: rows < 0 or cols < 0. Because we can't go left or top and
# we start at (0, 0). So we don't check those base cases.

# The height of the decision tree: We know every path leading to the target, is gonna have the same length. So any
# path in the decision tree is gonna have the same HEIGHT and the height or length is: number of rows + number of cols(n + m).
def bruteForce(r, c, rows, cols):
    # out of bounds
    if r == rows or c == cols:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1

    # r + 1: go down. c +1: go right
    return (bruteForce(r + 1, c, rows, cols) +
            bruteForce(r, c + 1, rows, cols))

print(bruteForce(0, 0, 4, 4))

# Memoization - DFS - top down DP(because we have memoization)
# Time and Space: O(n * m)
def memoization(r, c, rows, cols, cache):
    # It's important that we put this base case BEFORE the next base case. Otherwise, we could go out of bounds and
    # we tried to index the cache with invalid r or c and then we would get an exception.
    # Note: So we have to check if we went out of bounds BEFORE we try to index the cache.
    if r == rows or c == cols:
        return 0

    # Note: We can use a hashmap as cache as well. But here we used a 2-d arr.
    if cache[r][c] > 0:
        return cache[r][c]

    if r == rows - 1 and c == cols - 1:
        return 1

    # When we pass the cache in the func arg, we're not creating a new copy of it, we're passing the reference of it
    # to the next func call. We're reusing the cache throughout the recursive calls.
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) +
                   memoization(r, c + 1, rows, cols, cache))

    return cache[r][c]

print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))