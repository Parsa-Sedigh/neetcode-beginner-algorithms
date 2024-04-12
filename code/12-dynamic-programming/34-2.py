# Bottom-up approach(true DP)
# T: O(n * m)
# S: O(2 * m). So O(m) where m is number of cols. Why 2 * m? Because we have prevRow and curRow arrs.

# Start at the bottom(bottom right). At each iteration, we go through a row from right to left and at the bottom and
# work upwards.
def dp(rows, cols):
    # At the beginning, the prevRow is all zeroes. Because that's the row after the most bottom row and it doesn't
    # exist.
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1

        # we're starting at the second to last col. Why? Because we know the base case(target cell) is 1 anyway. We have filled in that
        # base case in the prev line of code.
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]

        prevRow = curRow

    return prevRow[0]

print(dp(4, 4))