class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        min_heap = sticks
        heapq.heapify(min_heap)
        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            combined = first + second
            res += combined
            heapq.heappush(min_heap, combined)
        return res



"""
`
res = 5 + 9 = 14
min_heap = [2,4,3]
2 + 3 -> 5 -> [4, 5]
4 + 5 -> 9 -> [9]


sticks = [1,8,3,5]
1 + 3 => 4 => [4,8,5]
4 + 5 => 9 => [9,8]
9 + 8 => 17 => [17]

`
"""