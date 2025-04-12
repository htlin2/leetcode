class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = [] #(count, char)
        for char, count in counter.items():
            heapq.heappush(max_heap, (-count, char))
        res = ''
        while len(max_heap) >= 2:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            res += first[-1] + second[-1]
            if first[0] + 1 != 0:
                heapq.heappush(max_heap, (first[0] + 1, first[-1]))
            if second[0] + 1 != 0:
                heapq.heappush(max_heap, (second[0] + 1, second[-1]))
        if max_heap and abs(max_heap[0][0]) > 1: return ''
        if max_heap and res and max_heap[0][-1] == res[-1]: return ''
        return res + max_heap[0][-1] if max_heap else res
"""
max_heap = (count, val)

"""