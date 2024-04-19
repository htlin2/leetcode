class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        # edge: return empty arr if impossible
        # build adj with {src: [dst1, dst2]}
        # dfs
        # base case:
            # if node has been visited return True
            # detect cycle and return empty arr
            # to loop through adj list
        # wrap dfs in a for loop from 0 ~ N
        adj = collections.defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        ans, visited, cycle = [], set(), set()
        def dfs(src):
            if src in visited: return True
            if src in cycle: return False
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei): return False
            cycle.remove(src)
            visited.add(src)
            ans.append(src)
            return True
        for i in range(N):
            if not dfs(i): return []
        return ans