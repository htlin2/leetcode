class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        res = []
        def dfs(src):
            stack = adj[src]
            while stack:
                nei = stack.pop()
                dfs(nei)
            res.append(src)
        dfs('JFK')
        return res[::-1]

"""
INPUT
[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
OUTPUT
["JFK","NRT","JFK","KUL"]

JFK: KUL, NRT
NRT: JFK

JFK -> KUL -> stop
"""