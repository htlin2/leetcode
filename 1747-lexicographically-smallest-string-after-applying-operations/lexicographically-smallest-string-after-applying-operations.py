class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = collections.deque([s])
        visited = set([s])
        res = s
        while q:
            for _ in range(len(q)):
                first = q.popleft()
                if int(first) <= int(res):
                    res = first
                arr_first = list(first)
                for i in range(len(res)):
                    if i % 2:
                        int_digit = (int(arr_first[i]) + a) % 10
                        str_digit = str(int_digit)
                        arr_first[i] = str_digit
                added_first = ''.join(arr_first)
                if added_first not in visited:
                    q.append(added_first)
                    visited.add(added_first)
                rotated_first = first[b:] + first[:b]
                if rotated_first not in visited:
                    q.append(rotated_first)
                    visited.add(rotated_first)
        return res