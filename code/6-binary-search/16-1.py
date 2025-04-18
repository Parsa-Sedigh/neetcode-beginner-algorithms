# Binary search on some range of values
# low is left pointer and high is right pointer
def binarySearch(low, high):
    while low <= high:
        mid = (low + high) // 2

        # returned 1, so mid is too big. Since the we're in a sorted situation, the target should be less than mid.
        # So move high to an earlier place(mid - 1).
        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid

        return -1


# Returns 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1

    if n < 10:
        return -1

    return 0
