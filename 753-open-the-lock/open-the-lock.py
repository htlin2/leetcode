class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_locks(lock):
            res = []
            for i in range(4):
                digit = int(lock[i])
                plus = lock[:i] + str((digit + 1) % 10) + lock[i+1:]
                minus = lock[:i] + str((digit - 1) % 10) + lock[i+1:]
                res.append(plus)
                res.append(minus)
            return res
        visited = set(deadends)
        if target in visited or '0000' in visited: return -1
        visited.add('0000')
        min_heap = [(0, '0000')]
        while min_heap:
            count, lock = heapq.heappop(min_heap)
            if lock == target: return count
            for nei in get_locks(lock):
                if nei in visited: continue
                visited.add(nei)
                heapq.heappush(min_heap, (count + 1, nei))
        return -1

"""
bfs - shortest path - prim's algorithm or districs?

"""
