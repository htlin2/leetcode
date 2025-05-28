class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(0, 0, 0, 1)] # time_, r, c, curr_move
        visited = set()
        while min_heap:
            time_, r, c, curr_move = heapq.heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1: return time_
            if (r, c, curr_move) in visited: continue
            visited.add((r, c, curr_move))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                next_move = 2 if curr_move == 1 else 1
                if (nr, nc, next_move) in visited: continue
                next_time = max(time_, grid[nr][nc]) + curr_move
                heapq.heappush(min_heap, (next_time, nr, nc, next_move))
        return -1
"""
msp
Input: moveTime = [
    [0,4],
    [4,4]
]


"""