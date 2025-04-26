class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.counts = [1] * N

    def find(self, n):
        if n == self.parents[n]: return n
        self.parents[n] = self.find(self.parents[self.parents[n]])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        c1, c2 = self.counts[p1], self.counts[p2]
        if c1 >= c2:
            self.counts[p1] += self.counts[p2]
            self.parents[p2] = p1
        else:
            self.counts[p2] += self.counts[p1]
            self.parents[p1] = p2
        return True

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        uf = UnionFind(ROWS)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    uf.union(r, c)
        parents = set([uf.find(i) for i in range(ROWS)])
        return len(parents)
"""
union find
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
[
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
[
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

[
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]


"""