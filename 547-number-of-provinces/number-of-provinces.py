class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.ranks = [1] * N

    def find(self, n):
        if self.parents[n] == n: return n
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1 and uf.union(i, j):
                    res += 1
        return N - res

"""
Input: isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

"""