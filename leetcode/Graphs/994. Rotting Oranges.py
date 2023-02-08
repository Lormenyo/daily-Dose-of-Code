import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        FRESH = 1
        ROTTEN = 2

            
        time = 0
        freshOranges = 0
        #add rotten oranges to queue and keep count of fresh oranges
        for r in range(rows):
            for c in range(cols):   
                if grid[r][c] == ROTTEN:
                    queue.append((r,c))
                if grid[r][c] == FRESH:
                    freshOranges += 1


        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and freshOranges > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != FRESH:
                        continue

                    grid[row][col] = ROTTEN
                    freshOranges -= 1
                    queue.append((row, col))
            time += 1

        return time if freshOranges == 0 else -1
