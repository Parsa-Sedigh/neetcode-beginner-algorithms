# Count paths(backtracking)
# Note: The visit param is gonna be a hashset DS.
# T: O(4 ^ (r * c))
# M: O(r * c)
def dfs(grid, r, c, visit):
    # Get the dimensions of the grid
    ROWS, COLS = len(grid), len(grid[0])

    # Base case 1
    if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit or grid[r][c] == 1):
        return 0

    # Base case 2
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)  # move down
    count += dfs(grid, r - 1, c, visit)  # move up
    count += dfs(grid, r, c + 1, visit)  # move right
    count += dfs(grid, r, c - 1, visit)  # move left

    visit.remove((r, c))

    return count


print(dfs(grid, 0, 0, set()))
