class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list) # idx1: [(distance, idx2)]
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        visited = set() # idx
        res = 0
        min_heap = [(0, 0)]
        while len(visited) < len(points):
            distance, idx = heapq.heappop(min_heap)
            if idx in visited:
                continue
            visited.add(idx)
            res += distance
            for nei in adj[idx]:
                if nei[-1] in visited:
                    continue
                heapq.heappush(min_heap, nei)
        return res
"""
graph + min_heap (BFS)
{
    0: [(4, 1), (13, 2), (7, 3), (7, 4)], 
    1: [(9, 2), (3, 3), (7, 4)], 
    2: [(10, 3), (14, 4)],
    3: [(4, 4)]
}
visited: (0, 1, 2)
heap: (10, 2), (11, 3), (9, 2)
total = 13
"""