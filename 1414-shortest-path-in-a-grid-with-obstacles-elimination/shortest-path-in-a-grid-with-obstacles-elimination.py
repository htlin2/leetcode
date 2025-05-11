class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if k >= ROWS + COLS - 2:
            return ROWS + COLS - 2
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # (r, c)
        q = collections.deque([(0, 0, k)]) # (r, c, rem_k, count)
        visited = set((0, 0, k))
        count = 0
        while q:
            for _ in range(len(q)):
                r, c, rem_k = q.popleft()
                if r == ROWS - 1 and c == COLS - 1: return count
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
                    if grid[nr][nc] == 1 and not rem_k: continue
                    new_k = rem_k - 1 if grid[nr][nc] == 1 else rem_k
                    if (nr, nc, new_k) in visited: continue
                    q.append((nr, nc, new_k))
                    visited.add((nr, nc, new_k))
            count += 1
        return -1
"""
[
    [0,0],
    [1,0],
    [1,0],
    [1,0],
    [1,0],
    [1,0],
    [0,0],
    [0,1],
    [0,1],
    [0,1],
    [0,0],
    [1,0],
    [1,0],
    [0,0]
    ]
"""