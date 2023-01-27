import collections

#this solution only passes 26/58 test cases
# fails with this test case: board = [["X","O","X"],["X","O","X"],["X","O","X"]]
# it returns [["X","O","X"],["X","X","X"],["X","O","X"]] instead of [["X","O","X"],["X","O","X"],["X","O","X"]]
# if i modify the checkforX function to check if the 0s are surrounded by X, then it means
# i will be adding 16 conditions (since the 0 has to be surroundered by ) at least 2 Xs
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def checkForX(i, j):
            return board[i-1][j] == "X" or board[i+1][j] == "X" or board[i][j+1] == "X" or board[i][j-1] == "X"

        def bfs(r, c):
            queue = collections.deque()

            queue.append((r, c))

            visited.add((r, c))

            board[r][c] = "X"

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col
                      

                    if newRow < (rows-1) and newCol < (cols-1) and board[newRow][newCol] == "O" and (newRow, newCol) not in visited and newRow != 0 and newRow != 0 and newCol != cols-1 and newRow != rows-1:
                        board[newRow][newCol] = "X"

                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))



        #find the zero surrounded by x, flip to x
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited and r != 0 and c != 0 and c != cols-1 and r != rows-1 and checkForX(r,c):
                    bfs(r, c)



class RealSolution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        # USING THE REVERSE THINKING APPROACH
        # CAPTURE EVERYTHING EXCEPT THE UNSURROUNDED REGIONS

        def dfs(r, c):
            #if region is out of bounds, or the region is not O, then ignore
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return

            board[r][c] = "T"
            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        # mark all unsurrounded regions at the border as T
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows -1 or c == cols -1:
                    dfs(r, c)

        # flip all remaining Os in Xs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #flip the Ts into Os
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

