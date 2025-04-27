class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = collections.deque([s])
        visited = set()
        visited.add(s)
        res = s
        while q:
            for _ in range(len(q)):
                first = q.popleft()
                if first < res:
                    res = first
                # add
                first_arr = list(first)
                for i in range(0, len(s), 2):
                    if i + 1 < len(s):
                        str_num = (int(first_arr[i + 1]) + a) % 10
                        first_arr[i + 1] = str(str_num)
                first_str = ''.join(first_arr)
                if first_str not in visited:
                    q.append(first_str)
                    visited.add(first_str)
                # rotate
                rotated = first[-b:] + first[:-b]
                if rotated not in visited:
                    q.append(rotated)
                    visited.add(rotated)
        return res