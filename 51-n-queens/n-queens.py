class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = []
        for i in range(n):
            row = ['.'] * n
            grid.append(row)

        row = set()
        col = set()
        positive_diag = set() # r + c
        negative_diag = set() # r - c

        def is_valid(r, c):
            # check row
            if r in row: return False
            # check col
            if c in col: return False
            # check diag
            if (r + c) in positive_diag: return False
            if (r - c) in negative_diag: return False
            return True

        res = []
        def backtrack(c):
            if c >= n:
                copy_grid = [''.join(row) for row in grid]
                res.append(copy_grid)
                return
            for r in range(n):
                if not is_valid(r, c): continue
                grid[r][c] = 'Q'
                row.add(r)
                col.add(c)
                positive_diag.add(r + c)
                negative_diag.add(r - c)

                backtrack(c + 1)

                grid[r][c] = '.'
                row.remove(r)
                col.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)
        backtrack(0)
        return res

"""

[    0123
   0".Q..",
   1"...Q",
   2"Q...",
   3"..Q."
]
row:2, col: 0
invalid (1,1) (0,2) positive_diag => (2),(2) =>  row + col
invalid (3,1) (2,0) negative_diag => (2),(2) =>  row - col

"""