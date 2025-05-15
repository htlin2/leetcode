class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for src, dst, weight in times:
            adj[src].append((weight, dst))
        min_heap = [(0, k)]
        shortest = {}
        while min_heap:
            weight, dst = heapq.heappop(min_heap)
            if dst in shortest: continue
            shortest[dst] = weight
            for nei_weight, nei in adj[dst]:
                if nei in shortest: continue
                heapq.heappush(min_heap, (weight + nei_weight, nei))
        if len(shortest) != n: return -1
        return max(shortest.values())