class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        adj = collections.defaultdict(set)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    adj[i].add(j)
                    adj[j].add(i)
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        res = 0
        for i in range(N):
            if i in visited: continue
            dfs(i)
            res += 1 
        return res

"""
Input: isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

"""