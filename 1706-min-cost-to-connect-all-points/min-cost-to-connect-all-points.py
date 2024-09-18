import collections, heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list) # src: [(weight, dst)]
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][-1] - points[j][-1])
                adj[i].append((weight, j))
                adj[j].append((weight, i))
        shortest = collections.defaultdict(int) # src: total_weight
        min_heap = [(0, 0)]
        while min_heap and len(shortest) < N:
            weight, dst = heapq.heappop(min_heap)
            if dst in shortest: continue
            shortest[dst] = weight
            for nei_weight, nei_dst in adj[dst]:
                if nei_dst in shortest: continue
                heapq.heappush(min_heap, (nei_weight, nei_dst))
        return sum(shortest.values())
        