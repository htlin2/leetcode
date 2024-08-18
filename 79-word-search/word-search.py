class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        if not word: return True
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() # (r, c)
        def dfs(r, c, idx):
            if idx >= len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: 
                return False
            if (r, c) in visited: return False
            if grid[r][c] != word[idx]: return False
            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, idx + 1):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
"""
backtracking
ABCCED
[A,B,C,E],
[S,F,C,S],
[A,D,E,E]

"""