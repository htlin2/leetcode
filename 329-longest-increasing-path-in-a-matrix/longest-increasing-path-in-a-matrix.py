class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROW, COL = len(grid), len(grid[0])
        memo = collections.defaultdict(int) # (r, c): max_count
        def dfs(r, c):
            if (r, c) in memo: return memo[r, c]
            res = 1
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if rr >= ROW or rr < 0 or cc >= COL or cc < 0:
                    continue
                if grid[r][c] > grid[rr][cc]:
                    res = max(dfs(rr, cc) + 1, res)
            memo[r, c] = res
            return res
        longest = 0
        for r in range(ROW):
            for c in range(COL):
                longest = max(longest, dfs(r, c))
        return longest

"""
BFS
Input: matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
Output: 4
vistied = (0, 2, 1)
q = [9] (r, c, count)

DFS
(r, c)
"""