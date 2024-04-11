# bottom-up DP approach
# T: O(n). Roughly n
# M: O(2). If we maintain an arr to the size of input, it's O(n). But this is not necessary. We can
# maintain an arr of 2 els. So: O(1)
def fibo_bottom_up(n):
    if n < 2:
        return n

    # We need to ONLY maintain the two prev elements, not the entire arr. Since we're doing bottom-up, initially,
    # we have 0 and 1 as the els.
    dp = [0, 1]
    i = 2

    while i <= n:
        # To calculate the next element, we only need 2 prev elements.
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1

    return dp[1]

print(fibo_with_memoization_bottom_up(5))