class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = [] #(count, char)
        for char, count in counter.items():
            heapq.heappush(max_heap, (-count, char))
        res = ''
        while max_heap:
            first = heapq.heappop(max_heap)
            if res and res[-1] == first[-1]:
                return ''
            res += first[-1]
            second = []
            if max_heap:
                second = heapq.heappop(max_heap)
                res += second[-1]
            if first[0] + 1 != 0:
                heapq.heappush(max_heap, (first[0] + 1, first[-1]))
            if second and second[0] + 1 != 0:
                heapq.heappush(max_heap, (second[0] + 1, second[-1]))
        return res
"""
max_heap = (count, val)

"""