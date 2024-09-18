class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list) # src: [(weight, dst)]
        for src, dst, weight in times:
            adj[src].append((weight, dst))
        if not adj[k]: return -1
        time = 0
        visited = set() # n
        min_heap = [(0, k)] # (weight, dst)
        while min_heap:
            weight, dst = heapq.heappop(min_heap)
            if dst in visited: continue
            time = max(weight, time)
            visited.add(dst)
            for nei_wei, nei_dst in adj[dst]:
                if nei_dst in visited: continue
                heapq.heappush(min_heap, (nei_wei + time, nei_dst))
        if len(visited) != n:
            return -1
        return time