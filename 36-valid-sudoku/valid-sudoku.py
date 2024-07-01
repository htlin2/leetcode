class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        r_map = collections.defaultdict(set)
        c_map = collections.defaultdict(set)
        d_map = collections.defaultdict(set)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.': continue
                if board[r][c] in r_map[r]: return False
                if board[r][c] in c_map[c]: return False
                r_map[r].add(board[r][c])
                c_map[c].add(board[r][c])
                
                d_r = r // 3
                d_c = c // 3
                if board[r][c] in d_map[d_r, d_c]: return False
                d_map[d_r, d_c].add(board[r][c])
        return True