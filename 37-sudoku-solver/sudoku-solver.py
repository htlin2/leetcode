class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, num):
            for i in range(9):
                # check row
                if board[r][i] == num: return False
                # check col
                if board[i][c] == num: return False
                # check square
                row = (r // 3) * 3 + i // 3
                col = (c // 3) * 3 + i % 3
                if board[row][col] == num: return False
            return True

        def dfs(r, c):
            if r == 9: return True
            if c == 9: return dfs(r + 1, 0)
            if board[r][c] == '.':
                for i in range(1, 10):
                    if is_valid(r, c, str(i)):
                        board[r][c] = str(i)
                        if dfs(r, c + 1): return True
                        board[r][c] = '.'
                return False
            else:
                return dfs(r, c + 1)
        return True if dfs(0, 0) else False