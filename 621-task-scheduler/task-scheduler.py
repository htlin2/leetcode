import collections, heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)
        q = collections.deque() # (-count, cooling_time)
        time = 0
        while q or max_heap:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][-1] == time:
                count, _ = q.popleft()
                heapq.heappush(max_heap, count)
        return time


"""
max heap + q
"""