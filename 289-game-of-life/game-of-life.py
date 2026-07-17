class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        b,a
        0,0: 0
        1,0: 1
        0,1: 2
        1,1: 3
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROW, COL = len(board), len(board[0])        
        for r in range(ROW):
            for c in range(COL):
                live_count = 0
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if rr < 0 or cc < 0 or rr >= ROW or cc >= COL: continue
                    if board[rr][cc] in [1, 3]:
                        live_count += 1
                is_alive = board[r][c] in [1, 3]
                if is_alive and live_count < 2:
                    board[r][c] = 1
                elif is_alive and 2 <= live_count <= 3:
                    board[r][c] = 3
                elif is_alive and 3 < live_count:
                    board[r][c] = 1
                elif not is_alive and live_count == 3:
                    board[r][c] = 2

        for r in range(ROW):
            for c in range(COL):
                cell = board[r][c]
                if cell == 1:
                    board[r][c] = 0
                elif cell in [2,3]:
                    board[r][c] = 1
