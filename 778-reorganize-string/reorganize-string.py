class Solution:
    def reorganizeString(self, s: str) -> str:
        # solution 2 max_heap
        N = len(s)
        counter = collections.Counter(s)
        max_key = max(counter, key=lambda k: counter[k])
        if counter[max_key] > math.ceil(N / 2): return ''

        ans = []
        max_heap = [[-val, key] for key, val in counter.items()]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            ans.append(first[-1])
            ans.append(second[-1])
            first[0] += 1
            second[0] += 1
            if first[0] != 0:
                heapq.heappush(max_heap, first)
            if second[0] != 0:
                heapq.heappush(max_heap, second)
        if max_heap:
            first = heapq.heappop(max_heap)
            if first[0] > 1: return ''
            ans.append(first[-1])
        return ''.join(ans) if len(ans) == N else ''