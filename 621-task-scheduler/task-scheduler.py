class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [-v for v in counter.values()]
        heapq.heapify(max_heap)
        q = collections.deque() # (count, time)
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][-1] == time:
                count, _ = q.popleft()
                heapq.heappush(max_heap, count)
        return time