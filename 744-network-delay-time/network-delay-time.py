class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for src, dst, time in times:
            adj[src].append((time, dst))
        min_heap = [(0, k)]
        hashmap = collections.defaultdict(int)
        while min_heap:
            time, dst = heapq.heappop(min_heap)
            if dst in hashmap: continue
            hashmap[dst] = time
            if len(hashmap) == n:
                break
            for nei_time, nei_dst in adj[dst]:
                if nei_dst in hashmap: continue
                heapq.heappush(min_heap, (time + nei_time, nei_dst))
        if len(hashmap) != n: return -1
        return max(hashmap.values())
