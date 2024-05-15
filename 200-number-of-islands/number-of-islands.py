class UF:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.ranks = [1] * N
    
    def find(self, n):
        if n == self.parents[n]: return n
        self.parents[n] = self.find(self.parents[self.parents[n]])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.ranks[p1] >= self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = self.parents[p1]
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = self.parents[p2]
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        uf = UF(ROWS * COLS)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0': continue
                count += 1
                n1 = r * COLS + c
                for dr, dc in directions:
                    rr, cc = dr + r, dc + c
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS: continue
                    if grid[rr][cc] == '0': continue
                    n2 = rr * COLS + cc
                    if uf.union(n1, n2):
                        count -= 1
        return count