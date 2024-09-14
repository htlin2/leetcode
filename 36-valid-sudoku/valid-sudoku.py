class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        row_map = collections.defaultdict(set) # row_num: set()
        col_map = collections.defaultdict(set) # col_num: set()
        diag_map = collections.defaultdict(set) # (row, col): set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                n = grid[r][c]
                if n == '.':
                    continue
                if n in row_map[r] or n in col_map[c]:
                    return False
                row_map[r].add(n)
                col_map[c].add(n)

                # check diag
                diag_tup = (r // 3, c // 3)
                if n in diag_map[diag_tup]:
                    return False
                diag_map[diag_tup].add(n)
        return True

"""
diag_map
row, col = 0, 3 => row // 3, col // 3  => (0, 1)
row, col = 3, 3 => row // 3, col // 3  => (1, 1)
row, col = 3, 2 => row // 3, col // 3  => (1, 0)
"""