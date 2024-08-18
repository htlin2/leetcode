class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        if not word: return True
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() # (r, c)
        found = False
        def dfs(r, c, idx):
            nonlocal found
            if found: return
            if idx >= len(word):
                found = True
                return
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return
            if (r, c) in visited: return
            if grid[r][c] != word[idx]: return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, idx + 1)
            visited.remove((r, c))
        
        idx = 0
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, idx)
        return found
"""
backtracking
ABCCED
[A,B,C,E],
[S,F,C,S],
[A,D,E,E]

"""