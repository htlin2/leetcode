import heapq, collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        res = []
        def dfs(src):
            while adj[src]:
                nei = heapq.heappop(adj[src])
                dfs(nei)
            res.append(src)
        dfs('JFK')
        return res[::-1]