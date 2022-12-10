# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        if not grid:
            return 0

        numberOfIslands = 0
        visitedLands = set()

        def bfs(i, j):
            queue = collections.deque()
            visitedLands.add((i, j))
            queue.append((i, j))

            while queue:
                r, c = queue.popleft()
                directions = [
                    [1, 0], #down
                    [-1 , 0], #up
                    [0, 1], #right
                    [0, -1] #left
                ]

                for di, dj in directions:
                    row, col = r+ di, c + dj
                    if (row) in range(len(grid)) and \
                    (col) in range(len(grid[0])) and \
                    grid[row][col] == "1" and \
                    (row, col) not in visitedLands:
                       queue.append((row, col))
                       visitedLands.add((row, col))
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)

                    numberOfIslands += 1

        return numberOfIslands
