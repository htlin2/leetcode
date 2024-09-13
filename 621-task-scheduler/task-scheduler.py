import collections, heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [(-count, key) for key, count in counter.items()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            temp = [] # (-count, key)
            for _ in range(n + 1):
                if not max_heap and not temp: return time
                time += 1
                if temp and not max_heap:
                    continue
                count, key = heapq.heappop(max_heap)
                count += 1
                if count == 0:
                    continue
                temp.append((count, key))
            for item in temp:
                heapq.heappush(max_heap, item)
        return time
"""
counter = {A: 0, B: 3}
max_heap = [(3, A),(4, B)] cooling_time, task
time = 3
A, B, idle
return time


Input: tasks = ["A","C","A","B","D","B"], n = 1
counter = {A: , B: 1, C: 0}
max_heap = [, (, B)]
time = 6
A,B,C,A,B

"""