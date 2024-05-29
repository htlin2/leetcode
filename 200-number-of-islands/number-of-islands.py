class UnionFind:
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
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        N = ROWS * COLS
        uf = UnionFind(N)
        success_count = 0
        ones_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0' or (r, c) in visited: continue
                ones_count += 1
                # visited.add((r, c))
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or cc < 0 or rr >= ROWS or cc >= COLS: continue
                    if (rr, cc) in visited or grid[rr][cc] == '0': continue
                    n1 = r * COLS + c
                    n2 = rr * COLS + cc
                    if uf.union(n1, n2):
                        success_count += 1
                    # visited.add((rr, cc))
        return ones_count - success_count

"""
1 DFS
iterate through grid
run dfs on 1
    increment count
    iterate through 4 directions
    check for out of bounds
    mark 1 to 0
    call dfs on 4 directions
return count

2 BFS
iterate through grid
when hitting 1 
increment count
run BFS
    iterate through 4 directions
    mark 1's to 0's
return count

3 Union Find
iterate through grid
    when hittin 1
    iterate through 4 directions
        union with original 1 from grid
        count how many successful unions
return R*C - successful unions
"""