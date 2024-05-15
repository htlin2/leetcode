class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        dp = []
        for row in mat:
            dp.append(row[:])
        for r in range(ROWS):
            for c in range(COLS):
                min_dist = float('inf')
                if dp[r][c] == 0: continue
                if r - 1 >= 0:
                    min_dist = min(min_dist, dp[r - 1][c])
                if c - 1 >= 0:
                    min_dist = min(min_dist, dp[r][c - 1])
                dp[r][c] = min_dist + 1
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                min_dist = float('inf')
                if dp[r][c] == 0: continue
                if r + 1 < ROWS:
                    min_dist = min(min_dist, dp[r + 1][c])
                if c + 1 < COLS:
                    min_dist = min(min_dist, dp[r][c + 1])
                dp[r][c] = min(min_dist + 1, dp[r][c])
        return dp

"""
1. BFS

2. dp
"""