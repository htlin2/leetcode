class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c
        grid = []
        for r in range(n):
            row = ['.'] * n
            grid.append(row)
        ans = []
        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in grid]
                ans.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag: continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                grid[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                grid[r][c] = '.'
        backtrack(0)
        return ans