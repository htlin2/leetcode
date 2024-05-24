class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.': continue
                if cell in rows[r]: return False
                if cell in cols[c]: return False
                rows[r].add(cell)
                cols[c].add(cell)

                sqr_tuple = (r // 3, c // 3)
                if cell in sqrs[sqr_tuple]: return False
                sqrs[sqr_tuple].add(cell)
        return True