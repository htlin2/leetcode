class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        res = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)
        dfs('JFK')
        return res[::-1]