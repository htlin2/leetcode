import collections, heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [(-count, task) for task, count in counter.items()]
        heapq.heapify(max_heap)
        q = collections.deque([])
        time = 0
        while q or max_heap:
            time += 1
            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    q.append((count, task, time + n))
            while q and q[0][-1] == time:
                count, task, _ = q.popleft()
                heapq.heappush(max_heap, (count, task))
        return time

"""
Input: tasks = ["A","A","A","B","B"], n = 2
max_heap = [(_, A), (_, B)] # count, task
q = [(2, A, 4), (1, B, 5)] # count, task, time + n + 1
time = 3
A -> B -> idle ->
1    2       3    
"""