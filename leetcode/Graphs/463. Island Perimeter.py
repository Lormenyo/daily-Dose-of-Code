

# You are given row x col grid representing a map where grid[i][j] = 1 r
# epresents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        visited = set()
       

        def dfs(i ,j):

            # if we are at the boundary(perimeter) or close to water
            # then add 1 to the perimeter
            if i >= len(grid) or j >= len(grid[0]) or \
            i< 0 or j<0 or grid[i][j] == 0:
                return 1

            #if already visited, add 0 to perimeter
            if (i,j) in visited:
                return 0

            visited.add((i, j)) # add position to visited set

            perimeter = dfs(i, j+1) # check cells to the right
            perimeter += dfs(i, j-1) # check cells to the left
            perimeter += dfs(i+1, j) # check cells down
            perimeter += dfs(i-1, j) # check cells up

            return perimeter

        # find the next available land to start from there
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)