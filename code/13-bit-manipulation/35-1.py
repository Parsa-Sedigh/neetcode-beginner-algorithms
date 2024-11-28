# given an int, count the number of `1` bits.
def countsBits(n):
    count = 0

    # we're assuming we're not dealing with negative numbers in this case.
    # This condition will be executed until n becomes 0, so sth like 000...0, in a 32 bit int.
    while n > 0:
        # if the bitwise and op is 1, it means the right most bit of n was 1, so we got a 1, increment the `count`
        if n & 1 == 1:
            count += 1

        # Note: we could do: n = n // 2
        # Note: we wanna get the number of 1 bits. So we're doing a bitwise & in each iteration. Now since bitwise & only looks
        # at the right most bit of n, we shift the bits of n to the right at each iteration, so that all of the bits of n,
        # are gonna get `bitwise &` with 1.
        # Note: Doing shift to left is completely wrong. Because by doing it, the bits go to the left and we for their prev
        # place, a 0 would appear and the left most bit would get chopped of and that 0 would get bitwise & with 1, which is wrong.
        n = n >> 1

    return count


print(countsBits(23))
