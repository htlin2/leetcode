class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list) # src: [dst1, dst2]
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        cycle, visited = set(), set()
        def dfs(i):
            if i in cycle: return False
            if i in visited: return True
            cycle.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            cycle.remove(i)
            visited.add(i)
            return True

        for i in range(N):
            if not dfs(i):
                return False

        return len(visited) == N