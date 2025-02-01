class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if target in visited or "0000" in visited: return -1
        def get_nei(nums):
            res = []
            for i in range(len(nums)):
                digit = (int(nums[i]) + 1) % 10
                res.append(nums[:i] + str(digit) + nums[i + 1:])
                digit = (int(nums[i]) - 1) % 10
                res.append(nums[:i] + str(digit) + nums[i + 1:])
            return res
        q = collections.deque([(0, "0000")]) # (count, combo)
        while q:
            count, combo = q.popleft()
            if combo == target: return count
            for nei in get_nei(combo):
                if nei in visited: continue
                visited.add(nei)
                q.append((count + 1, nei))
        return -1
"""
shortest path prim's algo (min_heap)
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

visited = ["0201","0101","0102","1212","2002", "0000", "0009"]
heap = [(1, 0001), (1, 0009), (1, 0010), (1, 0100), (1, 1000)]
Time: E * log(v)
Space: E + V
"""