class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = [] # (dist, x, y)
        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            dist_points.append((dist, x, y))
        heapq.heapify(dist_points)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(dist_points)
            res.append([x, y])
        return res
"""
min_heap
(distance, x, y)
time: O(n + k log n)
space: O(n)
"""