class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_nei(num):
            res = []
            for i in range(4):
                digit = (int(num[i]) + 1) % 10
                res.append(num[:i] + str(digit) + num[i+1:])
                digit = (int(num[i]) - 1 + 10) % 10
                res.append(num[:i] + str(digit) + num[i+1:])
            return res
        if "0000" in deadends:
            return -1
        q = collections.deque([(0, '0000')])
        visited = set(deadends)
        while q:
            count, num = q.popleft()
            if num == target:
                return count
            count += 1
            for nei in get_nei(num):
                if nei in visited:
                    continue
                visited.add(nei)
                q.append((count, nei))
        return -1

"""
BFS + Math
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

"""