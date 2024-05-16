class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [] # (dist, x, y)
        for x, y in points:
            dist = (x ** 2 + y ** 2)
            min_heap.append((dist, x, y))
        res = []
        heapq.heapify(min_heap)
        while min_heap and len(res) < k:
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        return res
"""
1. sorting
all_dist = [(dist, x, y)]
sort all_dist
iterate all_dist
return [(x, y)]

Time: O(n log n)
space: O(n)


2. min heap
all_dist = [(dist, x, y)]
min_heap = hepify(all_dist) #log n
res = []
while min_heap and len(res) < k:
    pop min_heap
    append to res
return res

Time: O(n)
space: O(n)
"""