from collections import deque


# T: O(r * c)
# M: O(r * c)
# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])

    # We have a visit hashset just like with DFS.
    # we need sort of a marker to mark the cells that we already visited so that we don't stuck in an infinite loop.
    # This hashset is for this task.
    # This visit hashset helps us with time complexity as well, because we won't visit the cells that we've already visited.
    visit = set()

    # We have a queue like BFS on tree. The queue is gonna tell us the current level that we're at
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0

    while queue:
        # Here, we take a snapshot of the length of the queue.
        # Note: At each time(layer of movement), we wanna pop all of the cells in the queue. We have to have this for loop.
        # Just note that range() takes a snapshot, so it won't evaluate the new queue as we add to it in the for loop. It would
        # only take a snapshot.
        for i in range(len(queue)):
            r, c = queue.popleft()

            # If we're at the destination, return the length of the path
            if r == ROWS - 1 and c == COLS - 1:
                return length

            # These are not actually the neighbors necessarily. These are the directions.
            # For example [0, 1] would represent the right direction, [0, -1] is left, [1, 0] below and [-1, 0] above
            # Note: These lines are kinda boilerplate to go through all 4 directions of the current node in the queue.
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # dr stands for difference in row. We're saying: How much the row changes?
            for dr, dc in neighbors:
                # We know we can move in 4 directions, just like we did in DFS and we know there's a bunch of edge cases like
                # we could go out of bounds. Or we could reach a position that is blocked. Or we could reach a position we've already
                # visited before. These are a few edge cases.
                # One out of bounds is: (min(r + dr, c + dc) < 0 and another one is r + dr == ROWS or c + dc == COLS
                # Note: We could have this conditional 4 times for all 4 directions. But another way to do it is to take all 4 of the neighbors.
                if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue

                queue.append((r + dr, c + dc))

                # Why we add to the visit hashset as soon as we add to the queue(previous line)? This is very important. This is why the
                # BFS algo runs in O(n * m). The time complexity is because we're never going to add the same position to the queue twice.
                # We're never going to visit the same position twice.
                # Because we're going layer by layer and we don't want to visit a position twice. When we have multiple positions to go to,
                # we add all of them and we make them visited and now in the next iteration, since we mark the neighbours of previos position
                # as visited, now in the new position, we won't be able to go them because we mark those neighbours as visited when we
                # were in the previous position. So adding to visit hashset as soon as adding to the queue, prevents visiting the
                # positions twice.
                visit.add((r + dr, c + dc))

        length += 1


print(bfs(grid))
