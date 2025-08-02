class Solution:
    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        ROWS, COLS = len(is_connected), len(is_connected[0])
        for r in range(ROWS):
            for c in range(COLS):
                if is_connected[r][c]:
                    adj[r].add(c)
        visited = set()
        count = 0
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in adj[node]:
                if nei in visited: continue
                dfs(nei)
            return
        for r in range(ROWS):
            if r not in visited:
                dfs(r)
                count += 1
        return count
"""
dfs
output 2
[
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

0: {0, 1}
1: {0, 1}
2: {2}

visited = 0, 1, 2
cycle = 0, 1, 2

1

"""