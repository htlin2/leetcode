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
            self.parents[p2] = p1
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = p2
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for src, dst in edges:
            if not uf.union(src, dst):
                return [src, dst]
        return []