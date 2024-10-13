class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        ROW, COL = len(grid), len(grid[0])
        N = len(word)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() # (r, c)
        def dfs(r, c, i):
            if i == N: return True
            if r < 0 or c < 0 or r >= ROW or c >= COL: return False
            if (r, c) in visited: return False
            if grid[r][c] != word[i]: return False
            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            visited.remove((r, c))
            return False
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0): return True
        return False
"""
Backtracking
Input: grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

[
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

"""