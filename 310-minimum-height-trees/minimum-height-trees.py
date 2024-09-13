class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(set)
        for src, dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        q = collections.deque([])
        edge_counts = {}
        for key, values in adj.items():
            if len(values) == 1:
                q.append(key)
            edge_counts[key] = len(values)
        while q:
            if n <= 2:
                return q
            for _ in range(len(q)):
                n -= 1
                node = q.popleft()
                for nei in adj[node]:
                    edge_counts[nei] -= 1
                    if edge_counts[nei] == 1:
                        q.append(nei)
        return [0]

"""
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
0: 1
1: [0, 2, 3]
2: 1
3: 1

Input: n = 6, edges = [[1,0],[1,2],[1,3],[4,2].[5,2]]
0: 1
1: [0, 2, 3]
2: 1, 4, 5
3: 1
4: 2
5: 2

    1
0   2   3
   4 5
 

   2
4 0 5
 1 3
output: 0, 2

1) dfs + track levels of tree
build adj
iterate throught adj
    run dfs


2) bfs + track levels
"""