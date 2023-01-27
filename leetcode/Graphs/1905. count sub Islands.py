
# do simultaneous dfs

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # the grids have the same size
        rows, columns = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            
            isLand = True
            # if it is out of bounds, or water or visited in grid2, return true
            if r < 0 or r == rows or c < 0 or c == columns or grid2[r][c] == 0 or (r, c) in visited:
                return True

            visited.add((r,c))
            # if is water in grid1, return false
            if grid1[r][c]:
                isLand = False

            # check if all 4 directions is land
            isLand = dfs(r - 1, c) and isLand
            isLand = dfs(r + 1, c) and isLand
            isLand = dfs(r, c - 1) and isLand
            isLand = dfs(r, c + 1) and isLand

            return isLand


        noOfSubIslands = 0
        for i in range(rows):
            for j in range(columns):
                if grid2[i][j] and (i,j) not in visited and dfs(i, j):
                    noOfSubIslands += 1

        return noOfSubIslands

