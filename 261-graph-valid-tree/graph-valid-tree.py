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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False
        for i in range(n):
            uf.parents[i] = uf.find(i)
        all_parents = set(uf.parents)
        return len(all_parents) == 1

"""
Union Find?

DFS / BFS
edge case, 2 roots
1 -> 2 -> 3
4 -> 5
not a valid tree

how to detec cycle?

example 2=
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
                                           i
0 -> 1 -> 2 -> 3
     1 -> 3 (x) return false

Time: O(n)
Space: O(n)

[
    [0,1],
    [2,3],
    [1,2]
]
0 -> 1
2 -> 3
1 -> 2
"""