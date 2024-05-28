class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        one_count = 0
        q = collections.deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    one_count += 1
        if not q and not one_count: return 0
        res = -1
        while q:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS: continue
                    if grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        q.append([rr, cc])
                        one_count -= 1
        return -1 if one_count else res

"""
[
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
BFS
get all rotten oranges and put in queue
run bfs to change fresh oranges to rotten
track how many counts
edge case: if there is still a 1, return -1 
return counts
"""