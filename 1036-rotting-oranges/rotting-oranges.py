class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        good_count = 0
        minutes = -1
        q = collections.deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    good_count += 1
                elif grid[row][col] == 2:
                    q.append([row, col])
        if not q and good_count:
            return -1
        if not q and not good_count:
            return 0
        while q:
            minutes += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    adj_row, adj_col = dr + row, dc + col
                    if not (0 <= adj_row < ROWS and 0 <= adj_col < COLS):
                        continue
                    if grid[adj_row][adj_col] != 1:
                        continue
                    grid[adj_row][adj_col] = 2
                    q.append([adj_row, adj_col])
                    good_count -= 1
        return minutes if good_count == 0 else -1