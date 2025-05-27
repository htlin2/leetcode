class Solution:
    def checkIfPrerequisite(self, N: int, prerequisites: List[List[int]], q: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
        def dfs(src, dst, cycle):
            if src == dst: return True
            if src in cycle: return False
            cycle.add(src)
            for nei in adj[src]:
                if dfs(nei, dst, cycle):
                    return True
            return False
        
        res = []
        for src, dst in q:
            res.append(dfs(src, dst, set()))
        return res
"""
"""