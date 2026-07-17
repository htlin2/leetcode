class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROW, COL = len(board), len(board[0])
        live_cells = set() # (r, c)
        for r in range(ROW):
            for c in range(COL):
                cell = board[r][c]
                if cell == 1:
                    live_cells.add((r, c))
        
        for r in range(ROW):
            for c in range(COL):
                live_count = 0
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if (rr, cc) in live_cells:
                        live_count += 1
                is_alive = board[r][c] == 1
                if is_alive and live_count < 2:
                    board[r][c] = 0
                elif is_alive and 2 <= live_count <= 3:
                    board[r][c] = 1
                elif is_alive and 3 < live_count:
                    board[r][c] = 0
                elif not is_alive and live_count == 3:
                    board[r][c] = 1