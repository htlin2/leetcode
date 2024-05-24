class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, num):
            for i in range(9):
                if board[r][i] == num: return False
                if board[i][c] == num: return False
                row = 3 * (r // 3) + i // 3
                col = 3 * (c // 3) + i % 3
                if board[row][col] == num: return False
            return True

        def dfs(r, c):
            if r == 9: return True
            if c == 9: return dfs(r + 1, 0)
            if board[r][c] == '.':
                for num in range(1, 10):
                    if is_valid(r, c, str(num)):
                        board[r][c] = str(num)
                        if dfs(r, c + 1): return True
                        board[r][c] = '.'
            else:
                return dfs(r, c + 1)
        return True if dfs(0, 0) else False